import pandas as pd

from settings import CLEANED_DATASET_DIR


class CleanedDatasets:
    def __init__(self, config: dict) -> None:
        self.config = config

    def get(
        self,
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        return self.get_train(), self.get_test()

    def get_train(self) -> pd.DataFrame:
        return self._load(
            self.config["cleaned_datasets"]["train"],
            "train",
        )

    def get_test(self) -> pd.DataFrame:
        return self._load(
            self.config["cleaned_datasets"]["test"],
            "test",
        )

    @staticmethod
    def _load(file_name: str, split_name: str) -> pd.DataFrame:
        path = CLEANED_DATASET_DIR / file_name

        if not path.exists():
            raise FileNotFoundError(
                f"[DATASET ERROR] "
                f"Cleaned {split_name} dataset not found: "
                f"{path}"
            )

        print(
            f"\nЗагрузка {split_name} раздела"
        )

        print(f"Загрузка {path}")

        dataset = pd.read_csv(path)

        print(
            f"Исходный размер: "
            f"{dataset.shape}"
        )

        return dataset