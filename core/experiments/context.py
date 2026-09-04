import json
from collections import Counter

import pandas as pd
from sklearn.model_selection import StratifiedKFold

from core.experiments.data import CleanedDatasets
from core.experiments.metadata import Metadata, MetadataError
from core.experiments.overview import HumanReadableDataset
from settings import CONFIGS_DIR, EXPERIMENTS_DIR


class Experiment:
    def __init__(self, name: str):
        self.name = name
        self.config = self._load_config()
        self.path = EXPERIMENTS_DIR / self.name

        self.cleaned_datasets = CleanedDatasets(self.config)
        self.overview = HumanReadableDataset(self.config)
        self._metadata = Metadata(self.config)


    @property
    def cleaned_datasets_config(self) -> dict:
        return self.config["cleaned_datasets"]

    @property
    def cross_validation_config(self) -> dict:
        return self.config["cross_validation"]

    @property
    def overview_config(self) -> dict:
        return self.config["structure"]

    @property
    def metadata(self) -> dict:
        try:
            return self._metadata.get()
        except ValueError:
            dataset = self.overview.get()

            raise MetadataError(
                f"\n[METADATA ERROR]\n"
                f"Необходимо разделить признаки на группы внутри config:\n"
                f"  - target\n"
                f"  - identifiers\n"
                f"  - numerical_features\n"
                f"  - categorical_features\n"
                f"  - ordinal_features\n"
                f"  - binary_features\n\n"
                f"Признаки текущего эксперимента будут выведены снизу:\n"
                f"{dataset.columns}\n"
            )

    @property
    def model_config(self) -> dict:
        return self.config["model"]

    @property
    def cross_validator(self):
        config = self.cross_validation_config

        if config["strategy"] == "StratifiedKFold":
            return StratifiedKFold(
                n_splits=config["n_splits"],
                shuffle=config["shuffle"],
                random_state=config["random_state"],
            )

        raise ValueError(
            f"Неизвестная стратегия cross-validation: "
            f"{config['strategy']}"
        )

    @classmethod
    def create(cls, name: str):
        pass
        # создать config из template
        # создать необходимые директории
        # вернуть Experiment

    def info(self) -> None:
        dataset = self.overview.get()

        self._print_dataset_info(dataset)

        structure = self.metadata
        self._metadata.print_metadata(structure)

    @classmethod
    def inspect_all(cls) -> None:
        experiment_names = cls._get_experiment_names()

        if not experiment_names:
            print("Эксперименты не найдены.")
            return

        print("Доступные эксперименты:\n")

        for name in experiment_names:
            print(
                f"\n{'=' * 60}"
                f"\nЭксперимент: {name}"
                f"\n{'=' * 60}"
            )

            cls(name).info()

    @staticmethod
    def _get_experiment_names() -> list[str]:
        return sorted(
            path.stem
            for path in CONFIGS_DIR.glob("*.json")
            if path.stem != "template"
        )

    @staticmethod
    def _print_dataset_info(
        dataset: pd.DataFrame,
    ) -> None:
        print(
            f"\nКоличество строк: "
            f"{len(dataset)}"
        )

        print(
            f"Количество признаков: "
            f"{dataset.shape[1]}"
        )

        dtype_counts = Counter(
            dataset.dtypes.astype(str)
        )

        print(
            "Типы данных: "
            + ", ".join(
                f"{dtype}({count})"
                for dtype, count in sorted(
                    dtype_counts.items()
                )
            )
        )

        memory_usage = dataset.memory_usage(
            index=True,
            deep=False,
        ).sum()

        print(
            f"Использование памяти: "
            f"{memory_usage / 1024:.1f} KB"
        )

    def _load_config(self) -> dict:
        path = CONFIGS_DIR / f"{self.name}.json"

        if not path.exists():
            raise FileNotFoundError(
                f"[CONFIG ERROR] Config not found: {path}"
            )

        try:
            with path.open(
                "r",
                encoding="utf-8",
            ) as file:
                return json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(
                f"[CONFIG ERROR] Invalid JSON config: {path}"
            ) from error