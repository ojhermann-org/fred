from collections.abc import Callable
import json
import os
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import pytest

type FredGetJson = Callable[[str, dict[str, str]], dict[str, Any]]
type FredGetXml = Callable[[str, dict[str, str]], ET.Element]

# FRED occasionally returns transient 500s on otherwise-valid requests
# (observed on geofred/series/group and series/vintagedates). Retry only on 500.
_RETRY_ATTEMPTS = 5
_RETRY_BACKOFF_SECONDS = 0.5


def _urlopen_with_retry(full_url: str) -> bytes:
    for attempt in range(1, _RETRY_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(full_url) as response:  # noqa: S310
                result: bytes = response.read()
                return result
        except urllib.error.HTTPError as exc:
            if exc.code != 500 or attempt == _RETRY_ATTEMPTS:
                raise
            time.sleep(_RETRY_BACKOFF_SECONDS * attempt)
    raise RuntimeError("unreachable")


@pytest.fixture
def api_key() -> str:
    key = os.environ.get("FRED_API_KEY", "")
    if not key:
        if os.environ.get("CI"):
            pytest.fail("FRED_API_KEY is not set")
        pytest.skip("FRED_API_KEY not set")
    return key


@pytest.fixture
def fred_get_json() -> FredGetJson:
    def _get(url: str, params: dict[str, str]) -> dict[str, Any]:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
        result: dict[str, Any] = json.loads(_urlopen_with_retry(full_url))
        return result

    return _get


@pytest.fixture
def fred_get_xml() -> FredGetXml:
    def _get(url: str, params: dict[str, str]) -> ET.Element:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
        return ET.fromstring(_urlopen_with_retry(full_url))

    return _get
