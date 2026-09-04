from dataclasses import dataclass
from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV


@dataclass
class TrainingResult:
    name: str
    strategy: str
    search: GridSearchCV

    @property
    def score(self) -> float:
        return self.search.best_score_

    @property
    def parameters(self) -> dict:
        return self.search.best_params_

    @property
    def estimator(self):
        return self.search.best_estimator_


class ResultsCollector:
    def __init__(self, experiment_path: Path) -> None:
        self.path = experiment_path
        self.results: list[TrainingResult] = []

    def add(self, result: TrainingResult) -> None:
        self.results.append(result)
        self._save_checkpoint(result)
        self.save_results()

    def load_checkpoint(self, name: str) -> TrainingResult | None:
        checkpoint_path = self._get_checkpoint_path(name)

        if not checkpoint_path.exists():
            return None

        return joblib.load(checkpoint_path)

    def to_dataframe(self) -> pd.DataFrame:
        data = [
            {
                "name": result.name,
                "strategy": result.strategy,
                "score": result.score,
                "parameters": result.parameters,
            }
            for result in self.results
        ]

        return (
            pd.DataFrame(data)
            .sort_values("score", ascending=False)
            .reset_index(drop=True)
        )

    def save_results(self) -> None:
        reports_path = (self.path / "reports")

        reports_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.to_dataframe().to_csv(
            reports_path / "results.csv",
            index=True,
        )

    def _save_checkpoint(self, result: TrainingResult) -> None:
        checkpoint_path = (
            self._get_checkpoint_path(result.name)
        )

        checkpoint_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            result,
            checkpoint_path,
        )

    def _get_checkpoint_path(self, name: str) -> Path:
        return self.path / "checkpoints" / f"{name}.joblib"