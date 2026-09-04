from pathlib import Path

import pandas as pd

from research.cleaning import TrainCleaner, TestCleaner
from research.schemas import TrainSchema, TestSchema

from settings import (
    RAW_DATASET_DIR,
    CLEANED_DATASET_DIR,
)


def create_clean_dataset(
    raw_path: Path,
    cleaned_path: Path,
    schema,
    cleaner,
):
    df = pd.read_csv(raw_path)

    df = schema.normalize(df)
    df = cleaner.clean(df)

    cleaned_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        cleaned_path,
        index=False,
    )


def main():
    create_clean_dataset(
        raw_path=RAW_DATASET_DIR / "train.csv",
        cleaned_path=CLEANED_DATASET_DIR / "train.csv",
        schema=TrainSchema,
        cleaner=TrainCleaner(),
    )

    create_clean_dataset(
        raw_path=RAW_DATASET_DIR / "test.csv",
        cleaned_path=CLEANED_DATASET_DIR / "test.csv",
        schema=TestSchema,
        cleaner=TestCleaner(),
    )


if __name__ == "__main__":
    main()