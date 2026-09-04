import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

from logging_system import TrainingLogger
from logging_system.decorators import log_experiment

from src.training.mode import TrainingMode
from training.result import TrainingResult


class ModelTrainer:
    def __init__(self, experiment) -> None:
        self.experiment = experiment
        self.logger = TrainingLogger()

    @log_experiment
    def train(
        self,
        name: str,
        pipeline: Pipeline,
        strategy: str,
        parameters: dict,
        train: pd.DataFrame,
        mode: TrainingMode,
    ) -> TrainingResult:
        X = train.drop(
            columns=[
                self.experiment.metadata["target"],
            ]
        )
        y = train[self.experiment.metadata["target"]]

        verbose = 2 if mode is TrainingMode.DEBUG else 0

        cross_validation = GridSearchCV(
            estimator=pipeline,
            param_grid=parameters,
            cv=self.experiment.cross_validator,
            scoring="accuracy",
            n_jobs=-1,
            verbose=verbose,
        )

        fit_params = {}

        model = pipeline.named_steps["model"]

        if hasattr(model, "get_cat_feature_indices"):
            fit_params["model__cat_features"] = [
                *self.experiment.metadata["categorical_features"],
                *self.experiment.metadata["ordinal_features"],
            ]

        cross_validation.fit(X, y, **fit_params)

        # if mode is TrainingMode.DEBUG:
        #     with self.logger.capture_output():
        #         cross_validation.fit(X, y, model__cat_features=cat_features)
        # else:
        #     cross_validation.fit(X, y, model__cat_features=cat_features)

        return TrainingResult(
            name=name,
            strategy=strategy,
            search=cross_validation,
        )