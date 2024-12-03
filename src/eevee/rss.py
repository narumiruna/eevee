import feedparser
import httpx


def fetch_feed(url: str) -> feedparser.FeedParserDict:
    """
    Fetches and parses an RSS feed from the given URL.

    Args:
        url (str): The URL of the RSS feed to fetch.

    Returns:
        feedparser.FeedParserDict: The parsed RSS feed.

    Raises:
        httpx.HTTPStatusError: If the HTTP request returned an unsuccessful status code.
    """
    with httpx.Client() as client:
        resp = client.get(url)
        resp.raise_for_status()
        return feedparser.parse(resp.text)
