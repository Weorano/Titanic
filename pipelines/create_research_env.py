import json
from pathlib import Path
from typing import Dict, Any

import pandas as pd

from settings import (
    RESEARCH_CONFIG_PATH,
    NOTEBOOKS_DIR,
    FULL_DATA_PROCESSING_NOTEBOOK,
    EXPERIMENTS_NOTEBOOK,
)

from src.research.core.notebook_template.creator import NotebookCreator

from src.research.core.notebook_template.notebook_spec import (
    EXPERIMENTS_SPEC, FULL_RESEARCH_STATE_1,
)

class ResearchEnvPipeline:
    def __init__(self):
        self.config: Dict[str, Any] = self._load_config()

    @staticmethod
    def _load_config() -> Dict[str, Any]:
        if not RESEARCH_CONFIG_PATH.exists():
            raise FileNotFoundError(
                f"[CONFIG ERROR] Config not found: "
                f"{RESEARCH_CONFIG_PATH}"
            )

        try:
            with RESEARCH_CONFIG_PATH.open("r",encoding="utf-8") as f:
                return json.load(f)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"[CONFIG ERROR] Invalid JSON config: {e}"
            )

    def _validate_config(self) -> None:
        """
        Checks the correctness of the configuration before launching the pipeline.
        Throws an exception for critical errors.
        """
        if "datasets_paths" not in self.config:
            raise ValueError(
                "[CONFIG ERROR] Before generating the notebook, "
                "you need to create the \"datasets_paths\" key in "
                "the configuration."
                "[CONFIG ERROR] Missing required keys: {missing_keys}"
            )

        # Проверка директории с тетрадками
        # Если её нет — значит структура фреймворка сломана
        if not NOTEBOOKS_DIR.exists():
            raise FileNotFoundError(
                "[FRAMEWORK ERROR] '/src/research/notebooks/' "
                "doesn't exist anymore. "
                "The framework structure is corrupted or outdated."
            )

        datasets = self.config["datasets_paths"]

        if len(datasets) == 0:
            raise ValueError(
                "[CONFIG ERROR] Before generating the notebook, "
                "you need to create the \"datasets_paths\" key in "
                "the configuration."
            )

        if not isinstance(datasets, dict):
            raise TypeError(
                "[CONFIG ERROR] 'datasets_paths' must be dict"
            )

        for name, path in datasets.items():
            if not isinstance(name, str):
                raise TypeError(
                    "[CONFIG ERROR] Dataset name must be string"
                )

            if not isinstance(path, str):
                raise TypeError(
                    f"[CONFIG ERROR] Dataset path for "
                    f"'{name}' must be string"
                )

    def validate_datasets(self) -> None:
        datasets = self.config["datasets_paths"]

        for name, path in datasets.items():
            p = Path(path)

            try:
                if p.exists():
                    pd.read_csv(p, nrows=5)
                else:
                    pd.read_csv(path, nrows=5)

            except Exception as e:
                raise ValueError(
                    f"[DATASET ERROR] dataset '{name}' not cant be read: {e}"
                )

    def create_notebooks(self) -> None:
        creator = NotebookCreator(config=self.config)

        self._create_full_data_processing_notebook(creator)
        self._create_experiments_notebook(creator)

    @staticmethod
    def _create_full_data_processing_notebook(creator: NotebookCreator) -> None:
        if FULL_DATA_PROCESSING_NOTEBOOK.exists():
            raise FileExistsError(
                f"[NOTEBOOK ERROR] "
                f"nt full_data_processing_notebook.ipynb"
                f" already exists. "
                f"Most likely the notebook generator "
                f"has already been launched before."
            )

        creator.create(
            spec=FULL_RESEARCH_STATE_1,
            notebook_path=FULL_DATA_PROCESSING_NOTEBOOK,
        )

    @staticmethod
    def _create_experiments_notebook(creator: NotebookCreator) -> None:
        if EXPERIMENTS_NOTEBOOK.exists():
            raise FileExistsError(
                f"[NOTEBOOK ERROR] "
                f"nt experiments.ipynb already exists. "
                f"Most likely the notebook generator "
                f"has already been launched before."
            )

        creator.create(
            spec=EXPERIMENTS_SPEC,
            notebook_path=EXPERIMENTS_NOTEBOOK,
        )

    def run(self) -> bool:
        self._validate_config()
        self.validate_datasets()
        self.create_notebooks()

        return True