from collections.abc import Callable
import json
import os
from typing import Any
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import pytest

type FredGetJson = Callable[[str, dict[str, str]], dict[str, Any]]
type FredGetXml = Callable[[str, dict[str, str]], ET.Element]


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
        with urllib.request.urlopen(full_url) as response:  # noqa: S310
            result: dict[str, Any] = json.loads(response.read())
            return result

    return _get


@pytest.fixture
def fred_get_xml() -> FredGetXml:
    def _get(url: str, params: dict[str, str]) -> ET.Element:
        full_url = f"{url}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(full_url) as response:  # noqa: S310
            return ET.fromstring(response.read())

    return _get
