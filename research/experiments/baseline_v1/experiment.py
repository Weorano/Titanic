import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from core.experiments.context import Experiment
from core.experiments.observer import record

from feature_adapter import AdapterForLinear
from preprocessing import (
    AdvancedProcessingTransformer,
    SurfaceProcessingTransformer,
)
from src.training.mode import TrainingMode
from src.training.result import ResultsCollector, TrainingResult
from training.trainer import ModelTrainer


Preprocessing = list[tuple[str, TransformerMixin]]


class BaselineExperiment:

    def __init__(self) -> None:
        self.experiment = Experiment("baseline_v1")
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
