import json
from typing import Dict, Any

import pandas as pd

from settings import (
    RESEARCH_CONFIG_PATH,
    NOTEBOOKS_DIR,
    FULL_DATA_PROCESSING_NOTEBOOK,
)

from src.research.core.notebook_template.creator import NotebookCreator

from src.research.core.notebook_template.notebook_spec import (
    FULL_RESEARCH_STATE_2,
)

class PreprocessingBodyPipeline:
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

    @staticmethod
    def _validate() -> None:
        # Проверка директории с тетрадками
        # Если её нет — значит структура фреймворка сломана
        if not NOTEBOOKS_DIR.exists():
            raise FileNotFoundError(
                "[FRAMEWORK ERROR] '/src/research/notebooks/' "
                "doesn't exist anymore. "
                "The framework structure is corrupted or outdated."
            )

        # файл ноутбука существует (stage 1)
        if not FULL_DATA_PROCESSING_NOTEBOOK.exists():
            raise FileNotFoundError(
                "[NOTEBOOK ERROR] stage 1 notebook not found. "
                "Activate /pipelines/create_research_env.py"
            )

        # ноутбук не пустой
        with open(FULL_DATA_PROCESSING_NOTEBOOK, "r", encoding="utf-8") as f:
            nb = json.load(f)

        if "cells" not in nb or len(nb["cells"]) == 0:
            raise ValueError(
                "[NOTEBOOK ERROR] Start only /pipelines/create_research_env.py"
            )

    def _create_body_for_full_data_processing_notebook(
            self,
            loaded_dataframes: Dict[str, pd.DataFrame],
    ) -> None:
        creator = NotebookCreator(config=self.config)

        creator.create(
            spec=FULL_RESEARCH_STATE_2,
            notebook_path=FULL_DATA_PROCESSING_NOTEBOOK,
            loaded_dataframes=loaded_dataframes,
            first_create = False,
        )

    def run(self, loaded_dataframes):
        self._validate()
        self._create_body_for_full_data_processing_notebook(
            loaded_dataframes
        )

