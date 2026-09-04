import json
from pathlib import Path
from typing import Dict, Any, List

import pandas as pd

from context import NotebookContext
from registration import NotebookSpecification
from notebooks.templates.structural_elements.container import ContainerBuilder
from notebooks.templates.structural_elements.python_code import VisualizationCodeStructurer
from settings import NOTEBOOKS_DIR


class NotebookCreator:
    def __init__(self, datasets: Dict[str, Any]):
        self.datasets = datasets

    def create(
            self,
            notebook_obj: NotebookSpecification,
            loaded_dataframes: None | Dict[str, pd.DataFrame] = None,
            first_create: bool = True
    ) -> None:
        notebook_path = NOTEBOOKS_DIR / notebook_obj.name + ".ipynb"

        if first_create:
            self._create_empty_notebook(notebook_path)

        if loaded_dataframes is None:
            loaded_dataframes = self._load_dfs()

        ctx = self._generate_notebook_structure(loaded_dataframes, notebook_obj.sections)

        self._append_in_notebook_body(notebook_path, ctx)

    @staticmethod
    def _create_empty_notebook(notebook_path: Path) -> None:
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(
                {"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5},
                f,
            )

    def _load_dfs(self) -> Dict[str, pd.DataFrame]:
        return {
            name: pd.read_csv(path)
            for name, path in self.datasets.items()
        }

    def _generate_notebook_structure(
            self,
            loaded_dataframes: Dict[str, pd.DataFrame],
            spec: NotebookSpec,
    ) -> List[Dict[str, Any]]:
        ctx = NotebookContext(
            loaded_dataframes = loaded_dataframes,
            config = self.config,
            container_builder = ContainerBuilder(),
            visualization_code_structurer=VisualizationCodeStructurer(),
        )

        for section in spec.sections:
            section(ctx)

        return ctx.cells

    @staticmethod
    def _append_in_notebook_body(
            notebook_path: Path,
            cells: List[Dict[str, Any]],
    ) -> None:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        nb["cells"].extend(cells)

        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2, ensure_ascii=False)


