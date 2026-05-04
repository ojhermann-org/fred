from pydantic import ValidationError
import pytest

from fred import geofred_series_data


def _valid_observation(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "region": "Alabama",
        "code": "01",
        "value": 35559,
        "series_id": "ALPCPI",
    }
    base.update(overrides)
    return base


def _valid_meta(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "title": "2012 Per Capita Personal Income by State (Dollars)",
        "region": "state",
        "seasonality": "Not Seasonally Adjusted",
        "units": "Dollars",
        "frequency": "Annual",
        "data": {"2012-01-01": [_valid_observation()]},
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"meta": _valid_meta()}
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = geofred_series_data.Response.model_validate(_valid_response())
    assert r.meta.title.startswith("2012 Per Capita")
    assert r.meta.region == "state"
    assert r.meta.seasonality == "Not Seasonally Adjusted"
    assert r.meta.units == "Dollars"
    assert r.meta.frequency == "Annual"
    assert r.meta.data is not None
    assert "2012-01-01" in r.meta.data
    obs = r.meta.data["2012-01-01"][0]
    assert obs.region == "Alabama"
    assert obs.code == "01"
    assert obs.value == 35559.0
    assert obs.series_id == "ALPCPI"


@pytest.mark.contract_test
def test_accepts_int_value() -> None:
    r = geofred_series_data.Response.model_validate(
        _valid_response(
            meta=_valid_meta(data={"2012-01-01": [_valid_observation(value=100)]})
        )
    )
    assert r.meta.data is not None
    assert r.meta.data["2012-01-01"][0].value == 100.0


@pytest.mark.contract_test
def test_accepts_float_value() -> None:
    r = geofred_series_data.Response.model_validate(
        _valid_response(
            meta=_valid_meta(data={"2015-01-01": [_valid_observation(value=5.7)]})
        )
    )
    assert r.meta.data is not None
    assert r.meta.data["2015-01-01"][0].value == 5.7


@pytest.mark.contract_test
def test_accepts_multiple_dates() -> None:
    r = geofred_series_data.Response.model_validate(
        _valid_response(
            meta=_valid_meta(
                data={
                    "2010-01-01": [_valid_observation(value=33848)],
                    "2011-01-01": [_valid_observation(value=34879)],
                }
            )
        )
    )
    assert r.meta.data is not None
    assert sorted(r.meta.data.keys()) == ["2010-01-01", "2011-01-01"]


@pytest.mark.contract_test
def test_accepts_missing_data_field() -> None:
    meta = _valid_meta()
    del meta["data"]
    r = geofred_series_data.Response.model_validate(_valid_response(meta=meta))
    assert r.meta.data is None


@pytest.mark.contract_test
def test_rejects_missing_meta() -> None:
    with pytest.raises(ValidationError):
        geofred_series_data.Response.model_validate({})


@pytest.mark.contract_test
def test_rejects_missing_title() -> None:
    meta = _valid_meta()
    del meta["title"]
    with pytest.raises(ValidationError):
        geofred_series_data.Response.model_validate(_valid_response(meta=meta))


@pytest.mark.contract_test
def test_rejects_observation_missing_region() -> None:
    obs = _valid_observation()
    del obs["region"]
    with pytest.raises(ValidationError):
        geofred_series_data.Response.model_validate(
            _valid_response(meta=_valid_meta(data={"2012-01-01": [obs]}))
        )


@pytest.mark.contract_test
def test_rejects_non_numeric_value() -> None:
    with pytest.raises(ValidationError):
        geofred_series_data.Response.model_validate(
            _valid_response(
                meta=_valid_meta(
                    data={"2012-01-01": [_valid_observation(value="not-a-number")]}
                )
            )
        )
