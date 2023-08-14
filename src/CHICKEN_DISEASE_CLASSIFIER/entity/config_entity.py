from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionconfig:
    root_dir:Path
    source_dir:Path

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