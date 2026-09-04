from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline

from research.preprocessing import (
    SurfaceProcessingTransformer,
    AdvancedProcessingTransformer
)
from settings import RAW_DATASET_DIR, HR_DATASET_DIR


class HumanReadableDataset:
    def __init__(self, config: dict) -> None:
        self.config = config

    @property
    def path(self) -> Path:
        name = self.config['experiment_name']
        return HR_DATASET_DIR / name / f"{name}.parquet"

    def get(self) -> pd.DataFrame:
        if not self.exists():
            self.build()

        return self.load()

    def exists(self) -> bool:
        return self.path.exists()

    def build(self) -> pd.DataFrame:
        if self.exists():
            raise FileExistsError(
                "[DATASET ERROR] "
                f"Human-readable dataset already exists: "
                f"{self.path}"
            )

        dataset = self._load_raw_train_dataset()

        pipeline = Pipeline([
            ("surface_processing", SurfaceProcessingTransformer()),
            ("advanced_processing", AdvancedProcessingTransformer()),
        ])

        print("\nЗапуск Research Pipeline")
        pipeline.fit(dataset)
        final_research_dataset = pipeline.transform(dataset)
        print(f"Research pipeline отработал")

        self._save(final_research_dataset)

        return final_research_dataset

    def load(self) -> pd.DataFrame:
        if not self.exists():
            raise FileNotFoundError(
                "[DATASET ERROR] "
                f"Human-readable dataset not found: "
                f"{self.path}"
            )

        return pd.read_parquet(self.path)

    def _load_raw_train_dataset(self) -> pd.DataFrame:
        path = RAW_DATASET_DIR / self.config['raw_datasets']["train"]

        if not path.exists():
            raise FileNotFoundError(
                f"[DATASET ERROR] "
                f"Raw train dataset not found: "
                f"{path}"
            )

        print(
            f"\nЗагрузка train раздела"
        )

        print(f"Загрузка {path}")

        dataset = pd.read_csv(path)

        print(
            f"Исходный размер: "
            f"{dataset.shape}"
        )

        return dataset

    def _save(self, dataset: pd.DataFrame) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        dataset.to_parquet(
            self.path,
            index=False,
        )

        print(
            f"\nОбработанный датасет сохранён: "
            f"\n{self.path}"
        )