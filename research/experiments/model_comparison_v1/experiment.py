import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from sklearn.base import TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from core.experiments.context import Experiment
from core.experiments.observer import record
from feature_adapter import (
    AdapterForDistance,
    AdapterForLinear,
    AdapterForTree,
    AdapterForBoosting,
)
from preprocessing import (
    AdvancedProcessingTransformer,
    SurfaceProcessingTransformer,
)
from src.training.mode import TrainingMode
from src.training.result import ResultsCollector, TrainingResult
from src.training.trainer import ModelTrainer

Preprocessing = list[tuple[str, TransformerMixin]]


class ModelComparisonExperiment:

    def __init__(self) -> None:
        self.experiment = Experiment("model_comparison_v1")
        self.collector = ResultsCollector(
            self.experiment.path,
        )
        self.trainer = ModelTrainer(
            self.experiment,
        )

    def run(self) -> None:
        train, _ = self.experiment.cleaned_datasets.get()

        preprocessing = [
            (
                "surface_processing",
                SurfaceProcessingTransformer(),
            ),
            (
                "advanced_processing",
                AdvancedProcessingTransformer(),
            ),
            (
                "feature_adapter",
                AdapterForLinear(self.experiment.metadata),
            ),
        ]

        self.logistic_none(preprocessing, train)
        self.logistic_l1(preprocessing, train)
        self.logistic_l2(preprocessing, train)
        self.elastic_net(preprocessing, train)

        preprocessing = [
            (
                "surface_processing",
                SurfaceProcessingTransformer(),
            ),
            (
                "advanced_processing",
                AdvancedProcessingTransformer(),
            ),
            (
                "feature_adapter",
                AdapterForDistance(self.experiment.metadata),
            ),
        ]

        self.knn(preprocessing, train)

        preprocessing = [
            (
                "surface_processing",
                SurfaceProcessingTransformer(),
            ),
            (
                "advanced_processing",
                AdvancedProcessingTransformer(),
            ),
            (
                "feature_adapter",
                AdapterForTree(self.experiment.metadata),
            ),
        ]

        self.decision_tree(preprocessing, train)
        self.random_forest(preprocessing, train)

        preprocessing = [
            (
                "surface_processing",
                SurfaceProcessingTransformer(),
            ),
            (
                "advanced_processing",
                AdvancedProcessingTransformer(),
            ),
            (
                "feature_adapter", AdapterForBoosting()
            ),
        ]

        self.catboost(preprocessing, train)
        self.lightgbm(preprocessing, train)
        self.xgboost(preprocessing, train)

    @record
    def logistic_none(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="logistic_none",
            strategy="linear",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    LogisticRegression(
                        solver="lbfgs",
                        C=np.inf,
                        max_iter=1000,
                        random_state=42,
                    ),
                ),
            ]),
            parameters={},
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def logistic_l1(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="logistic_l1",
            strategy="linear",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    LogisticRegression(
                        solver="saga",
                        l1_ratio=1.0,
                        max_iter=6000,
                        random_state=42,
                    )
                )
            ]),
            parameters={
                "model__C": [0.01, 0.1, 1.0, 10.0],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def logistic_l2(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="logistic_l2",
            strategy="linear",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    LogisticRegression(
                        solver="lbfgs",
                        l1_ratio=0.0,
                        max_iter=3000,
                        random_state=42,
                    ),
                )
            ]),
            parameters={
                "model__C": [0.01, 0.1, 1.0, 10.0],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def elastic_net(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="elastic_net",
            strategy="linear",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    LogisticRegression(
                        solver="saga",
                        max_iter=6000,
                        random_state=42,
                    ),
                )
            ]),
            parameters={
                "model__C": [0.01, 0.1, 1.0, 10.0],
                "model__l1_ratio": [0.25, 0.5, 0.75],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def knn(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="knn",
            strategy="distance",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    KNeighborsClassifier(),
                )
            ]),
            parameters={
                "model__n_neighbors": [3, 5, 7, 9],
                "model__weights": [
                    "uniform",
                    "distance",
                ],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def decision_tree(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="decision_tree",
            strategy="tree",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    DecisionTreeClassifier(
                        random_state=42,
                    )
                )
            ]),
            parameters={
                "model__max_depth": [3, 5, 10, None],
                "model__min_samples_split": [2, 5, 10],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def random_forest(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="random_forest",
            strategy="tree",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    RandomForestClassifier(
                        random_state=42,
                        n_jobs=-1,
                    )
                )
            ]),
            parameters={
                "model__n_estimators": [100, 300],
                "model__max_depth": [5, 10, None],
                "model__min_samples_split": [2, 5],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def catboost(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="catboost",
            strategy="boosting",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    CatBoostClassifier(
                        verbose=False,
                        random_seed=42,
                    )
                )
            ]),
            parameters={
                "model__iterations": [200, 500],
                "model__depth": [4, 6, 8],
                "model__learning_rate": [0.03, 0.1],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def lightgbm(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="lightgbm",
            strategy="boosting",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    LGBMClassifier(
                        random_state=42,
                        verbosity=-1,
                    )
                )
            ]),
            parameters={
                "model__n_estimators": [100, 300],
                "model__max_depth": [-1, 5, 10],
                "model__learning_rate": [0.03, 0.1],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )

    @record
    def xgboost(
            self,
            preprocessing: Preprocessing,
            train: pd.DataFrame,
    ) -> TrainingResult:
        return self.trainer.train(
            name="xgboost",
            strategy="boosting",
            pipeline=Pipeline([
                *preprocessing,
                (
                    "model",
                    XGBClassifier(
                        random_state=42,
                        eval_metric="logloss",
                        enable_categorical=True,
                    )
                )
            ]),
            parameters={
                "model__n_estimators": [100, 300],
                "model__max_depth": [3, 6, 10],
                "model__learning_rate": [0.03, 0.1],
            },
            train=train,
            mode=TrainingMode.NORMAL,
        )
