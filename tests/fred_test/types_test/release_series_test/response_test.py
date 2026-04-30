from pydantic import ValidationError
import pytest

from fred import release_series
from fred.enums import SeasonalAdjustment, SeasonalAdjustmentShort, SortOrder
from fred.enums.order_by import ReleaseSeries as OrderBy


def _valid_series(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "BOMTVLM133S",
        "realtime_start": "2017-08-01",
        "realtime_end": "2017-08-01",
        "title": "U.S. Imports of Services - Travel",
        "observation_start": "1992-01-01",
        "observation_end": "2017-05-01",
        "frequency": "Monthly",
        "frequency_short": "M",
        "units": "Million of Dollars",
        "units_short": "Mil. of $",
        "seasonal_adjustment": "Seasonally Adjusted",
        "seasonal_adjustment_short": "SA",
        "last_updated": "2017-07-06 09:34:00-05",
        "popularity": 0,
        "group_popularity": 0,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2017-08-01",
        "realtime_end": "2017-08-01",
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
    r = release_series.Response.model_validate(_valid_response())
    assert r.realtime_start == "2017-08-01"
    assert r.realtime_end == "2017-08-01"
    assert r.order_by == OrderBy.series_id
    assert r.sort_order == SortOrder.asc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 1000
    assert len(r.series) == 1


@pytest.mark.contract_test
def test_series_maps_seriess_alias() -> None:
    r = release_series.Response.model_validate(
        _valid_response(seriess=[_valid_series(), _valid_series(id="BOPGEXP")])
    )
    assert len(r.series) == 2
    assert r.series[1].id == "BOPGEXP"


@pytest.mark.contract_test
def test_accepts_empty_series_list() -> None:
    r = release_series.Response.model_validate(_valid_response(seriess=[], count=0))
    assert r.series == []


@pytest.mark.contract_test
def test_series_seasonal_adjustment_parsed_as_enum() -> None:
    r = release_series.Response.model_validate(_valid_response())
    assert r.series[0].seasonal_adjustment == SeasonalAdjustment.yes


@pytest.mark.contract_test
def test_series_seasonal_adjustment_short_parsed_as_enum() -> None:
    r = release_series.Response.model_validate(_valid_response())
    assert r.series[0].seasonal_adjustment_short == SeasonalAdjustmentShort.sa


@pytest.mark.contract_test
def test_series_notes_can_be_none() -> None:
    r = release_series.Response.model_validate(
        _valid_response(seriess=[_valid_series(notes=None)])
    )
    assert r.series[0].notes is None


@pytest.mark.contract_test
def test_series_accepts_notes() -> None:
    r = release_series.Response.model_validate(
        _valid_response(seriess=[_valid_series(notes="Some notes.")])
    )
    assert r.series[0].notes == "Some notes."


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        release_series.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        release_series.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_seriess_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["seriess"]
        release_series.Response.model_validate(data)
