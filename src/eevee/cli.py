from __future__ import annotations

from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv

from .config import Config
from .hardfork import predict_hardfork
from .rss import fetch_feed


@click.command()
@click.option(
    "-c", "--config-file", type=click.Path(exists=True), default="config/default.yaml", help="Path to the config file"
)
def main(config_file: Path):
    load_dotenv(find_dotenv())
    cfg = Config.load(config_file)

    for url in cfg.rss_urls:
        print(f"Fetching {url}")
        rss = fetch_feed(url)

        feed_title = rss.get("feed", {}).get("title", "Unknown feed title")
        print(f"Feed title: {feed_title}")

        for entry in rss["entries"]:
            hardfork = predict_hardfork(str(entry))
            link = entry["link"]
            updated = entry["updated"]
            print(f"link: {link}")
            print(f"updated: {updated}")
            print(f"hardfork: {hardfork}")
            print("-" * 80)
            break

        print("=" * 80)
        break
