from __future__ import annotations

from typing import Final

from pydantic import BaseModel

from .hardfork import Hardfork

MAX_SUMMARY_LENGTH: Final[int] = 100


class Result(BaseModel):
    url: str
    title: str
    entries: list[EntryResult] = []

    def to_markdown(self) -> str:
        lines = [
            f"## [{self.title}]({self.url})",
            "",
        ]

        for entry in self.entries:
            lines += [entry.to_markdown()]

        return "\n".join(lines)


class EntryResult(BaseModel):
    link: str
    title: str
    updated: str
    summary: str
    hardfork: Hardfork

    def to_markdown(self) -> str:
        lines = [
            f"### {self.title} ({self.updated})",
            self.summary[:MAX_SUMMARY_LENGTH] + "..." if len(self.summary) > MAX_SUMMARY_LENGTH else self.summary,
            "",
            f"- 🔗 Link: {self.link}",
            self.hardfork.to_markdown(),
            "",
        ]
        return "\n".join(lines)


def to_markdown(results: list[Result]) -> str:
    return "# Hardfork Analysis\n\n" + "\n".join([result.to_markdown() for result in results])
