from datetime import date

import pytest

from builders.v1.sources.builder import ENDPOINT, Builder

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"


@pytest.mark.smoke_test
def test_build_defaults() -> None:
    result = Builder(api_key=VALID_KEY).build()
    assert result.url == ENDPOINT
    assert result.params == {
        "api_key": VALID_KEY,
        "file_type": "xml",
        "realtime_start": date.today().isoformat(),
        "realtime_end": date.today().isoformat(),
        "limit": "1000",
        "offset": "0",
        "order_by": "source_id",
        "sort_order": "asc",
    }
