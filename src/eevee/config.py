from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel

from .utils import load_yaml


class Config(BaseModel):
    rss_urls: list[str]

    @classmethod
    def load(cls, f: str | Path) -> Config:
        return cls.model_validate(load_yaml(f))
