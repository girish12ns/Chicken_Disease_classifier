from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionconfig:
    root_dir:Path
    source_dir:Path