import feedparser
import httpx


def fetch_feed(url: str) -> feedparser.FeedParserDict:
    resp = httpx.get(url)
    resp.raise_for_status()
    return feedparser.parse(resp.text)
