from pathlib import Path
from typing import Any

import yaml


def load_yaml(f: str | Path) -> Any:
    with Path(f).open() as fp:
        return yaml.safe_load(fp)
