import pandas as pd


class BaseSchema:
    RENAME_COLUMNS: dict[str, str] = {}
    ORDER_COLUMNS: list[str] = []

    @classmethod
    def normalize(cls, df: pd.DataFrame) -> pd.DataFrame:
        df = df.rename(columns=cls.RENAME_COLUMNS).copy()
        return df[cls.ORDER_COLUMNS]