from __future__ import annotations

from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseModel

from .config import Config
from .hardfork import Hardfork
from .hardfork import predict_hardfork
from .rss import fetch_feed


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
    hardfork: Hardfork

    def to_markdown(self) -> str:
        lines = [
            f"### {self.title} ({self.updated})",
            f"- 🔗 Link: {self.link}",
            f"- {'🔴' if self.hardfork.hardfork else '🟢'} Hardfork: {self.hardfork.hardfork}",
            f"- 📊 Confidence: {self.hardfork.confidence * 100}%",
            f"- 📝 Explanation: {self.hardfork.explanation}",
            "",
        ]
        return "\n".join(lines)


def to_markdown(results: list[Result]) -> str:
    return "# Hardfork Analysis\n\n" + "\n".join([result.to_markdown() for result in results])


@click.command()
@click.option(
    "-c",
    "--config-file",
    type=click.Path(exists=True, path_type=Path),
    default="config/default.yaml",
    help="Path to the config file",
)
@click.option(
    "-o",
    "--output-file",
    type=click.Path(exists=False, path_type=Path),
    default="output.md",
    help="Path to the output markdown file",
)
def main(config_file: Path, output_file: Path) -> None:
    load_dotenv(find_dotenv())
    cfg = Config.load(config_file)

    results: list[Result] = []
    for url in cfg.rss_urls:
        rss = fetch_feed(url)

        result = Result(url=url, title=rss["feed"]["title"])
        results.append(result)

        for entry in rss["entries"]:
            entry_result = EntryResult(
                link=entry["link"],
                title=entry["title"],
                updated=entry["updated"],
                hardfork=predict_hardfork(str(entry)),
            )
            print(entry_result)
            result.entries.append(entry_result)

            # Save to file
            with output_file.open(mode="w", encoding="utf-8") as fp:
                fp.write(to_markdown(results))
