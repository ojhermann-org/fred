import os

import pytest


@pytest.fixture
def api_key() -> str:
    key = os.environ.get("FRED_API_KEY", "")
    if not key:
        if os.environ.get("CI"):
            pytest.fail("FRED_API_KEY is not set")
        pytest.skip("FRED_API_KEY not set")
    return key
