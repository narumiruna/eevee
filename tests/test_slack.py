import pytest
from typing import Callable, Dict, Any
from eevee.slack import get_slack_channel, get_slack_client, post_slack_message


@pytest.fixture
def set_env(monkeypatch: pytest.MonkeyPatch) -> Callable[[Dict[str, str]], None]:
    def _set_env(env_vars):
        for key, value in env_vars.items():
            monkeypatch.setenv(key, value)

    return _set_env


@pytest.fixture(autouse=True)
def clear_cache() -> None:
    get_slack_client.cache_clear()
    get_slack_channel.cache_clear()


def test_get_slack_client(set_env: Callable[[Dict[str, str]], None]) -> None:
    set_env({"SLACK_TOKEN": "test-token"})
    client = get_slack_client()
    assert client is not None
    assert client.token == "test-token"


def test_get_slack_client_no_token(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SLACK_TOKEN", raising=False)
    client = get_slack_client()
    assert client is None


def test_get_slack_channel(set_env: Callable[[Dict[str, str]], None]) -> None:
    set_env({"SLACK_CHANNEL": "test-channel"})
    channel = get_slack_channel()
    assert channel == "test-channel"


def test_get_slack_channel_no_channel(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SLACK_CHANNEL", raising=False)
    channel = get_slack_channel()
    assert channel is None


@pytest.fixture
def mock_slack_client(mocker: Any) -> Any:
    return mocker.patch("eevee.slack.get_slack_client")


@pytest.fixture
def mock_slack_channel(mocker: Any) -> Any:
    return mocker.patch("eevee.slack.get_slack_channel")


def test_post_slack_message(mock_slack_client: Any, mock_slack_channel: Any, mocker: Any) -> None:
    mock_slack_channel.return_value = "test-channel"
    mock_client = mocker.MagicMock()
    mock_slack_client.return_value = mock_client

    post_slack_message("Hello, world!")
    mock_client.chat_postMessage.assert_called_once_with(channel="test-channel", text="Hello, world!", mrkdwn=True)


def test_post_slack_message_no_client(mock_slack_client: Any, mock_slack_channel: Any) -> None:
    mock_slack_client.return_value = None
    mock_slack_channel.return_value = "test-channel"

    post_slack_message("Hello, world!")
    mock_slack_client.assert_called_once()


def test_post_slack_message_no_channel(mock_slack_client: Any, mock_slack_channel: Any) -> None:
    mock_slack_channel.return_value = None

    post_slack_message("Hello, world!")
    mock_slack_client.assert_called_once()
