import json
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


def load_json(f: str | Path) -> Any:
    with open(f) as fp:
        return json.load(fp)


def save_json(obj: Any, f: str | Path) -> None:
    with open(f, "w", encoding="utf-8") as fp:
        json.dump(obj, fp, indent=4, ensure_ascii=False)
