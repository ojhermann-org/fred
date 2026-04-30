from pydantic import ValidationError
import pytest

from fred import series_updates
from fred.enums.filter_value import SeriesUpdates as FilterValue
from fred.enums.sort_order import SortOrder


def _valid_series(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "PCPI06037",
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "title": "Per Capita Personal Income in Los Angeles County, CA",
        "observation_start": "1969-01-01",
        "observation_end": "2012-01-01",
        "frequency": "Annual",
        "frequency_short": "A",
        "units": "Dollars",
        "units_short": "$",
        "seasonal_adjustment": "Not Seasonally Adjusted",
        "seasonal_adjustment_short": "NSA",
        "last_updated": "2013-04-28 17:40:02-05",
        "popularity": 0,
        "group_popularity": None,
        "notes": None,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-13",
        "realtime_end": "2013-08-13",
        "filter_variable": "geography",
        "filter_value": "regional",
        "order_by": "last_updated",
        "sort_order": "desc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "seriess": [_valid_series()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = series_updates.Response.model_validate(_valid_response())
    assert r.filter_value == FilterValue.regional
    assert r.sort_order == SortOrder.desc
    assert len(r.seriess) == 1


@pytest.mark.contract_test
def test_accepts_macro_filter_value() -> None:
    r = series_updates.Response.model_validate(_valid_response(filter_value="macro"))
    assert r.filter_value == FilterValue.macro


@pytest.mark.contract_test
def test_accepts_empty_seriess() -> None:
    r = series_updates.Response.model_validate(_valid_response(seriess=[], count=0))
    assert r.seriess == []


@pytest.mark.contract_test
def test_rejects_missing_seriess() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["seriess"]
        series_updates.Response.model_validate(data)
