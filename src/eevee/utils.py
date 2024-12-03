from pathlib import Path
from typing import Any

import yaml


def load_yaml(f: str | Path) -> Any:
    """
    Load and parse a YAML file.

    Args:
        f (str | Path): The file path to the YAML file.

    Returns:
        Any: The parsed YAML content.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    with Path(f).open() as fp:
        return yaml.safe_load(fp)
