from pydantic import ValidationError
import pytest

from fred import series


def _valid_series(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "GNPCA",
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "title": "Real Gross National Product",
        "observation_start": "1947-01-01",
        "observation_end": "2013-01-01",
        "frequency": "Annual",
        "frequency_short": "A",
        "units": "Billions of Chained 2009 Dollars",
        "units_short": "Bil. of Chn. 2009 $",
        "seasonal_adjustment": "Not Seasonally Adjusted",
        "seasonal_adjustment_short": "NSA",
        "last_updated": "2013-07-31 09:26:16-05",
        "popularity": 39,
        "group_popularity": 39,
        "notes": "BEA Account Code: A001RX1",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "seriess": [_valid_series()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = series.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-14"
    assert len(r.seriess) == 1
    assert r.seriess[0].id == "GNPCA"


@pytest.mark.contract_test
def test_accepts_null_group_popularity() -> None:
    r = series.Response.model_validate(
        _valid_response(seriess=[_valid_series(group_popularity=None)])
    )
    assert r.seriess[0].group_popularity is None


@pytest.mark.contract_test
def test_accepts_null_notes() -> None:
    r = series.Response.model_validate(
        _valid_response(seriess=[_valid_series(notes=None)])
    )
    assert r.seriess[0].notes is None


@pytest.mark.contract_test
def test_accepts_empty_seriess() -> None:
    r = series.Response.model_validate(_valid_response(seriess=[]))
    assert r.seriess == []


@pytest.mark.contract_test
def test_rejects_missing_seriess() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["seriess"]
        series.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        series.Response.model_validate(_valid_response(realtime_start="not-a-date"))
