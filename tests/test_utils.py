import pytest
import yaml

from eevee.utils import load_yaml


def test_load_yaml_with_valid_file(tmp_path):
    yaml_content = """
    key1: value1
    key2: value2
    """
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml_content)

    result = load_yaml(yaml_file)
    assert result == {"key1": "value1", "key2": "value2"}


def test_load_yaml_with_invalid_file(tmp_path):
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text("invalid: [unclosed")

    with pytest.raises(yaml.YAMLError):
        load_yaml(yaml_file)


def test_load_yaml_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_yaml("nonexistent.yaml")
