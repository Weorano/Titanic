import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class SurfaceProcessingTransformer(BaseEstimator, TransformerMixin):
    STEPS = (
        "fill_missing_embarked",
        "optimize_dtypes",
    )

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        df = X.copy()

        for step in self.STEPS:
            df = getattr(self, step)(df)

        return df

    @staticmethod
    def fill_missing_embarked(df: pd.DataFrame) -> pd.DataFrame:
        df["embarked"] = df["embarked"].fillna("S")

        return df

    @staticmethod
    def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
        """
        См. 01_Preprocessing notebook:
        Раздел `Оптимизация данных`
        """

        df["passenger_id"] = (
            df["passenger_id"].astype("uint16")
        )

        df["sex"] = (
            df["sex"].astype("category")
        )

        df["age"] = (
            df["age"].astype("float32")
        )

        df["same_importance_relatives"] = (
            df["same_importance_relatives"]
            .astype("uint8")
        )

        df["high_importance_relatives"] = (
            df["high_importance_relatives"]
            .astype("uint8")
        )

        df["category_significance"] = (
            df["category_significance"]
            .astype("category")
        )

        if "survived" in df.columns:
            df["survived"] = (
                df["survived"].astype("int8")
            )

        df["embarked"] = (
            df["embarked"].astype("category")
        )

        return df