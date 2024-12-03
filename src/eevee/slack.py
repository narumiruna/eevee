import os
from functools import cache

from loguru import logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


@cache
def get_slack_client() -> WebClient | None:
    """
    Retrieves a Slack WebClient instance using the SLACK_TOKEN environment variable.

    Returns:
        WebClient | None: A Slack WebClient instance if the SLACK_TOKEN environment variable is set,
                          otherwise None.

    Logs:
        Warning: If the SLACK_TOKEN environment variable is not set.
    """
    token = os.getenv("SLACK_TOKEN")
    if token is None:
        logger.warning("SLACK_TOKEN environment variable is not set")
        return None

    return WebClient(token=token)


@cache
def get_slack_channel() -> str | None:
    """
    Retrieves the Slack channel from the environment variable.

    Returns:
        str | None: The Slack channel if the environment variable is set, otherwise None.

    Logs a warning if the SLACK_CHANNEL environment variable is not set.
    """
    channel = os.getenv("SLACK_CHANNEL")
    if channel is None:
        logger.warning("SLACK_CHANNEL environment variable is not set")
        return None

    return channel


def post_slack_message(text: str) -> None:
    """
    Posts a message to a Slack channel.

    This function retrieves the Slack channel and client, and then attempts to post
    a message to the specified channel. If the channel or client is not available,
    the function will return without posting the message. If an error occurs while
    posting the message, it will be logged.

    Args:
        text (str): The message text to be posted to the Slack channel.

    Returns:
        None
    """
    channel = get_slack_channel()
    client = get_slack_client()

    if channel is None or client is None:
        return

    try:
        client.chat_postMessage(channel=channel, text=text, mrkdwn=True)
    except SlackApiError as e:
        logger.error("Slack API error: {}", e)
