from pydantic import ValidationError
import pytest

from fred import series_search
from fred.enums.order_by import SeriesSearch as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_series(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "MSIM2",
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "title": "Monetary Services Index: M2 (preferred)",
        "observation_start": "1967-01-01",
        "observation_end": "2013-06-01",
        "frequency": "Monthly",
        "frequency_short": "M",
        "units": "Billions of Dollars",
        "units_short": "Bil. of $",
        "seasonal_adjustment": "Seasonally Adjusted",
        "seasonal_adjustment_short": "SA",
        "last_updated": "2013-07-31 09:26:16-05",
        "popularity": 34,
        "group_popularity": None,
        "notes": None,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "order_by": "search_rank",
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
    r = series_search.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.search_rank
    assert r.sort_order == SortOrder.desc
    assert len(r.seriess) == 1


@pytest.mark.contract_test
def test_accepts_empty_seriess() -> None:
    r = series_search.Response.model_validate(_valid_response(seriess=[], count=0))
    assert r.seriess == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        series_search.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_missing_seriess() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["seriess"]
        series_search.Response.model_validate(data)
