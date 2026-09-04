from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
)


class AdapterForDistance(
    BaseEstimator,
    TransformerMixin,
):
    def __init__(
        self,
        metadata: dict,
    ):
        self.metadata = metadata
        self.transformer = None

    def fit(self, X, y=None):
        self.transformer = ColumnTransformer(
            transformers=[
                (
                    "categorical",
                    OneHotEncoder(
                        handle_unknown="ignore",
                        sparse_output=False,
                    ),
                    self.metadata[
                        "categorical_features"
                    ],
                ),
                (
                    "ordinal",
                    OrdinalEncoder(
                        handle_unknown="use_encoded_value",
                        unknown_value=-1,
                    ),
                    self.metadata[
                        "ordinal_features"
                    ],
                ),
                (
                    "numerical",
                    StandardScaler(),
                    self.metadata[
                        "numerical_features"
                    ],
                ),
            ],
            remainder="passthrough",
        )

        self.transformer.fit(X, y)

        return self

    def transform(self, X):
        return self.transformer.transform(X)