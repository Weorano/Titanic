from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

CONFIGS_DIR = PROJECT_ROOT / "configs"
DATASETS_DIR = PROJECT_ROOT / "datasets"
NOTEBOOKS_DIR = PROJECT_ROOT / "src" / "research" / "notebooks"

FULL_DATA_PROCESSING_NOTEBOOK = (
    NOTEBOOKS_DIR / "full_data_processing.ipynb"
)

EXPERIMENTS_NOTEBOOK = (
    NOTEBOOKS_DIR / "experiments.ipynb"
)

RESEARCH_CONFIG_PATH = CONFIGS_DIR / "research_config.json"
