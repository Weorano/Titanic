from dataclasses import dataclass, field
from typing import Dict, Any, List
import pandas as pd

from .structural_elements.container import ContainerBuilder
from .structural_elements.python_code import VisualizationCodeStructurer


@dataclass
class NotebookContext:
    loaded_dataframes: Dict[str, pd.DataFrame]
    config: Dict[str, Any]
    container_builder: ContainerBuilder
    visualization_code_structurer: VisualizationCodeStructurer
    cells: List[Dict[str, Any]] = field(default_factory=list)
