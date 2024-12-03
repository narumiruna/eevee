import feedparser
import httpx
import pytest

from eevee.rss import fetch_feed


def test_fetch_feed_success(httpx_mock):
    url = "https://example.com/feed"
    httpx_mock.add_response(
        method="GET",
        url=url,
        status_code=200,
        text="<rss><channel><title>Example Feed</title></channel></rss>",
    )
    feed = fetch_feed(url)
    assert isinstance(feed, feedparser.FeedParserDict)
    assert feed["feed"]["title"] == "Example Feed"


def test_fetch_feed_http_error(httpx_mock):
    url = "https://example.com/feed"
    httpx_mock.add_response(
        method="GET",
        url=url,
        status_code=404,
    )
    with pytest.raises(httpx.HTTPStatusError):
        fetch_feed(url)
