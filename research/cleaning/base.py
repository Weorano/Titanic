import pandas as pd


class BaseCleaner:
    STEPS: tuple[str, ...] = ()

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        for step in self.STEPS:
            df = getattr(self, step)(df)

        return df