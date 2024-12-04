from __future__ import annotations

from typing import Final

from markdownify import markdownify as md
from pydantic import BaseModel

from .hardfork import Hardfork

MAX_SUMMARY_LENGTH: Final[int] = 500


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

    def to_slack(self) -> str:
        lines = [
            f"*<{self.url}|{self.title}>*",
            "",
        ]
        for entry in self.entries:
            lines.append(entry.to_slack())
        return "\n".join(lines)


class EntryResult(BaseModel):
    link: str
    title: str
    updated: str
    summary: str
    hardfork: Hardfork

    def format_summary_for_display(self) -> str:
        s = md(self.summary)  # Convert to markdown
        s = s[:MAX_SUMMARY_LENGTH] + "..." if len(s) > MAX_SUMMARY_LENGTH else s  # Trim to max length
        s = "```" + s + "```"  # Wrap in code block
        return s

    def to_markdown(self) -> str:
        lines = [
            f"### {self.title} ({self.updated})",
            self.format_summary_for_display(),
            "",
            f"- 🔗 Link: {self.link}",
            self.hardfork.to_markdown(),
            "",
        ]
        return "\n".join(lines)

    def to_slack(self, feed_title: str | None = None) -> str:
        lines = [
            f"*{feed_title}*: *{self.title}* ({self.updated})" if feed_title else f"*{self.title}* ({self.updated})",
            self.format_summary_for_display(),
            "",
            f"- 🔗 Link: {self.link}",
            self.hardfork.to_slack(),
            "",
        ]
        return "\n".join(lines)


def to_markdown(results: list[Result]) -> str:
    return "# Hardfork Analysis\n\n" + "\n".join([result.to_markdown() for result in results])


def to_slack(results: list[Result]) -> str:
    return "*Hardfork Analysis*\n\n" + "\n".join([result.to_slack() for result in results])
