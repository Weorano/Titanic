from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

CONFIGS_DIR = PROJECT_ROOT / "configs"

DATASETS_DIR = PROJECT_ROOT / "datasets"
RAW_DATASET_DIR = DATASETS_DIR / "01_raw"
CLEANED_DATASET_DIR = DATASETS_DIR / "02_cleaned"
HR_DATASET_DIR = DATASETS_DIR / "03_human_readable"

NOTEBOOKS_DIR = PROJECT_ROOT / "research" / "notebooks"

LOG_DIR = PROJECT_ROOT / "src" / "logs"
LOG_TRAINING_INFO = LOG_DIR / "training.log"
LOG_TRAINING_DEBUG = LOG_DIR / "training_debug.log"

EXPERIMENTS_DIR = PROJECT_ROOT / "research" / "experiments"