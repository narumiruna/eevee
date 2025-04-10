from loguru import logger

from . import redis
from .config import Config
from .hardfork import predict_hardfork
from .result import EntryResult
from .rss import fetch_feed
from .slack import post_slack_message
from .utils import parse_datetime


def get_entry_key(entry: dict) -> str:
    return f"eevee:{entry["id"]}:{entry['updated']}"


class App:
    def __init__(self, config: Config) -> None:
        self.config = config
        logger.debug(f"App initialized with config: {self.config}")

    def is_new_entry(self, entry: dict) -> bool:
        key = get_entry_key(entry)
        logger.debug(f"Checking if entry is new: {key}")

        if not redis.exists(key):
            logger.debug(f"Entry is new: {key}")
            return True

        updated_at = parse_datetime(entry["updated"])
        prev_updated_at = parse_datetime(redis.get(key))
        is_new = updated_at > prev_updated_at
        logger.debug(f"Entry {key} is new: {is_new}")
        return is_new

    def run(self):
        logger.debug("App run started")

        feeds = []
        for url in self.config.rss_urls:
            try:
                feeds.append(fetch_feed(url))
            except Exception as e:
                logger.error(f"Failed to fetch RSS feed from {url}: {e}")
                continue

        for feed in feeds:
            logger.debug(f"Processing feed: {feed}")

            feed_title = feed["feed"]["title"]
            for entry in feed["entries"]:
                if not self.is_new_entry(entry):
                    logger.debug(f"Skipping entry: {entry['id']}")
                    continue

                entry_result = EntryResult(
                    link=entry["link"],
                    title=entry["title"],
                    updated=entry["updated"],
                    summary=entry["summary"],
                    hardfork=predict_hardfork(str(entry)),
                )
                logger.debug(f"Entry result: {entry_result}")

                post_slack_message(entry_result.to_slack(feed_title))
                logger.debug("Posted to Slack")

                redis.set(get_entry_key(entry), entry["updated"])
                logger.debug(f"Updated redis with key: {get_entry_key(entry)}")

        logger.debug("App run completed")
