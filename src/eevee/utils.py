import json
from datetime import datetime
from pathlib import Path
from typing import Any

import dateparser
import yaml


def parse_datetime(s: str) -> datetime:
    # return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
    dt = dateparser.parse(s)
    if dt is None:
        raise ValueError(f"Could not parse datetime: {s}")
    return dt


def format_datetime(s: str) -> str:
    # return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
    return parse_datetime(s).strftime("%Y-%m-%d %H:%M:%S")


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
    """
    Load a JSON file and return its contents.

    Args:
        f (str | Path): The file path to the JSON file.

    Returns:
        Any: The contents of the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(f) as fp:
        return json.load(fp)


def save_json(obj: Any, f: str | Path) -> None:
    """
    Save a Python object as a JSON file.

    Args:
        obj (Any): The Python object to be serialized to JSON.
        f (str | Path): The file path where the JSON data will be saved.

    Returns:
        None
    """
    with open(f, "w", encoding="utf-8") as fp:
        json.dump(obj, fp, indent=4, ensure_ascii=False)
