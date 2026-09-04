from pathlib import Path

import pandas as pd

from artifacts.config_loader import Config

from notebooks.registration import (
    NOTEBOOK_PROJECT_OVERVIEW,
    NOTEBOOK_PREPROCESSING,
    NOTEBOOK_EDA,
    NOTEBOOK_ADVANCED_PROCESSING
)

from settings import (
    NOTEBOOKS_DIR,
)

from notebooks.creator import NotebookCreator


class ResearchEnvironment:
    def __init__(self, experiment_name: str) -> None:
        self.config = Config(experiment_name)

    def _validate_config(self) -> None:
        """
        Checks the correctness of the configuration before launching the pipeline.
        Throws an exception for critical errors.
        """

        # Проверка директории с тетрадками
        # Если её нет — значит структура фреймворка сломана
        if not NOTEBOOKS_DIR.exists():
            raise FileNotFoundError(
                "[FRAMEWORK ERROR] '/src/research/notebooks/' "
                "doesn't exist anymore. "
                "The framework structure is corrupted or outdated."
            )

        try:
            datasets_section = self.config.get_section(
                "raw_datasets",
            )
            if len(datasets_section) == 0:
                raise ValueError(
                    "[CONFIG ERROR] Before generating the notebook, "
                    "you need put train paths"
                )

            if not isinstance(datasets_section, dict):
                raise TypeError(
                    "[CONFIG ERROR] \"raw_datasets\" must be dict"
                )

        except ValueError as error:
            raise ValueError(
                "[CONFIG ERROR] Before generating the notebook, "
                "you need to create the \"raw_datasets\" key in "
                "the experiment configuration file and put paths."
                "[CONFIG ERROR] Missing required keys: \"raw_datasets\""
            ) from error

        try:
            datasets = datasets_section['train']

            if len(datasets) == 0:
                raise ValueError(
                    "[CONFIG ERROR] Before generating the notebook, "
                    "you need put minimum 1 path"
                )

            if not isinstance(datasets, dict):
                raise TypeError(
                    "[CONFIG ERROR] \"raw_datasets\" must be dict"
                )

        except ValueError as error:
            raise ValueError(
                "[CONFIG ERROR] Before generating the notebook, "
                "you need to create the \"train\" key in "
                "the experiment configuration file and put paths."
                "[CONFIG ERROR] Missing required keys: \"train\""
            ) from error

    def _validate_datasets(self) -> None:
        datasets_section = self.config.get_section("raw_datasets")
        datasets = datasets_section['train']

        for name, path in datasets.items():
            p = Path(path)

            if not isinstance(name, str):
                raise TypeError(
                    "[CONFIG ERROR] Dataset name must be string"
                )

            if not isinstance(path, str):
                raise TypeError(
                    f"[CONFIG ERROR] Dataset path for "
                    f"'{name}' must be string"
                )

            try:
                if p.exists():
                    pd.read_csv(p, nrows=5)
                else:
                    pd.read_csv(path, nrows=5)

            except Exception as e:
                raise ValueError(
                    f"[DATASET ERROR] dataset '{name}' not cant be read: {e}"
                )

    def _create_notebooks(self) -> None:
        # Проверяем не созданы ли уже тетрадки
        if any(NOTEBOOKS_DIR.iterdir()):
            raise FileExistsError(
                f"[NOTEBOOK ERROR] "
                f"Directory '{NOTEBOOKS_DIR}' is not empty. "
                f"Most likely the notebook generator "
                f"has already been launched before."
            )

        creator = NotebookCreator(
            self.config.get_section(
                "raw_datasets",
            )
        )

        creator.create(NOTEBOOK_PROJECT_OVERVIEW)
        creator.create(NOTEBOOK_PREPROCESSING)
        creator.create(NOTEBOOK_EDA)
        creator.create(NOTEBOOK_ADVANCED_PROCESSING)

def create(self) -> str:
    self._validate_config()
    self._validate_datasets()
    self._create_notebooks()

    return 'Тетрадки созданы успешно!'
