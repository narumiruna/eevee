import functools
import os
from typing import Any
from typing import cast

import redis
import redis.connection


@functools.cache
def get_redis_client() -> redis.Redis:
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    db = int(os.getenv("REDIS_DB", 0))

    return redis.Redis(
        host=host,
        port=port,
        db=db,
        charset="utf-8",
        decode_responses=True,
    )


def exists(key: str) -> Any:
    client = get_redis_client()
    res = client.exists(key)
    return cast(Any, res)


def set(key: str, value: str | int) -> Any:
    client = get_redis_client()
    res = client.set(key, value)
    return cast(Any, res)


def get(key: str) -> Any:
    client = get_redis_client()
    res = client.get(key)
    return cast(Any, res)
