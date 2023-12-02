from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    ElasticNet: str
    alpha: float
    l1_ratio: float
    DecisionTree: str
    criterion: str
    max_depth: int
    splitter: str
    min_samples_split: int
    min_samples_leaf: int
    min_weight_fraction_leaf:float
    max_features: str
    target_column: str




@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    ElasticNet_path: Path
    DecisionTree_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str