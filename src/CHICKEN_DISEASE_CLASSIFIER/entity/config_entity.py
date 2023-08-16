from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionconfig:
    root_dir:Path
    source_dir:Path
    category_1_dir: Path 
    category_2_dir: Path
    category_3_dir: Path
    category_4_dir: Path

@dataclass(frozen=True)
class Base_Model:
    root_dir:Path
    base_model_dir:Path
    updated_base_model_dir:Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class CallBacks:
    root_dir:Path
    tensorboard_root_log_dir:Path
    checkpoint_model_filepath:Path

@dataclass(frozen=True)
class Model_train:
    root_dir:Path
    trained_model_path:Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

