from pydantic import ValidationError
import pytest

from fred import tags_series
from fred.enums.order_by import TagsSeries as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_series(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "SLOFOOD",
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "title": "Food Price Index for Slovenia",
        "observation_start": "1991-01-01",
        "observation_end": "2013-06-01",
        "frequency": "Monthly",
        "frequency_short": "M",
        "units": "Index 2005=100",
        "units_short": "Index 2005=100",
        "seasonal_adjustment": "Not Seasonally Adjusted",
        "seasonal_adjustment_short": "NSA",
        "last_updated": "2013-07-31 09:26:01-05",
        "popularity": 0,
        "group_popularity": 0,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "order_by": "series_id",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "seriess": [_valid_series()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = tags_series.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.series_id
    assert r.sort_order == SortOrder.asc
    assert len(r.seriess) == 1
    assert r.seriess[0].id == "SLOFOOD"


@pytest.mark.contract_test
def test_accepts_series_with_notes() -> None:
    r = tags_series.Response.model_validate(
        _valid_response(seriess=[_valid_series(notes="Some notes.")])
    )
    assert r.seriess[0].notes == "Some notes."


@pytest.mark.contract_test
def test_accepts_empty_seriess() -> None:
    r = tags_series.Response.model_validate(_valid_response(seriess=[], count=0))
    assert r.seriess == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        tags_series.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_missing_seriess() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["seriess"]
        tags_series.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        tags_series.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )
