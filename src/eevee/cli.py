from __future__ import annotations

from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv

from .app import App
from .config import Config
from .hardfork import predict_hardfork
from .result import EntryResult
from .result import Result
from .result import to_markdown
from .rss import fetch_feed


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option(
    "-c",
    "--config-file",
    type=click.Path(exists=True, path_type=Path),
    default="config/default.yaml",
    help="Path to the config file",
)
def bot(config_file: Path) -> None:
    load_dotenv(find_dotenv())
    config = Config.load(config_file)

    app = App(config)
    app.run()


@cli.command()
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
def export(config_file: Path, output_file: Path) -> None:
    """
    Process RSS feeds and save the results to a file.

    This function reads the content of RSS feeds specified in a configuration file,
    processes each feed to determine if it contains a hardfork, and saves the results
    to an output file.
    """
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
