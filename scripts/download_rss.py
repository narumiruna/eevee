from pathlib import Path

from eevee.config import Config
from eevee.rss import fetch_feed
from eevee.utils import save_json


def build_filename(s: str, ext: str = ".json") -> str:
    s = s.replace("-", "")
    s = s.replace(" ", "_")
    s = s.replace("__", "_")
    return s.lower() + ext


def main() -> None:
    """Fetch RSS feeds and save to JSON files"""

    output_dir = Path("samples/rss")
    output_dir.mkdir(parents=True, exist_ok=True)

    config = Config.load("config/default.yaml")

    for url in config.rss_urls:
        data = fetch_feed(url)
        f = output_dir / build_filename(data["feed"]["title"])
        save_json(data, f)


if __name__ == "__main__":
    main()
