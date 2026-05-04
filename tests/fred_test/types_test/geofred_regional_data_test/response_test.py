from pydantic import ValidationError
import pytest

from fred import geofred_regional_data


def _valid_observation(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "region": "Alabama",
        "code": "01",
        "value": 35706,
        "series_id": "ALPCPI",
    }
    base.update(overrides)
    return base


def _valid_meta(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "title": "2013 Per Capita Personal Income by State (Dollars)",
        "region": "state",
        "seasonality": "Not Seasonally Adjusted",
        "units": "Dollars",
        "frequency": "Annual",
        "data": {"2013-01-01": [_valid_observation()]},
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"meta": _valid_meta()}
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = geofred_regional_data.Response.model_validate(_valid_response())
    assert r.meta.title.startswith("2013 Per Capita")
    assert r.meta.region == "state"
    assert r.meta.data is not None
    obs = r.meta.data["2013-01-01"][0]
    assert obs.region == "Alabama"
    assert obs.value == 35706.0


@pytest.mark.contract_test
def test_accepts_float_value() -> None:
    r = geofred_regional_data.Response.model_validate(
        _valid_response(
            meta=_valid_meta(data={"2015-01-01": [_valid_observation(value=6.09)]})
        )
    )
    assert r.meta.data is not None
    assert r.meta.data["2015-01-01"][0].value == 6.09


@pytest.mark.contract_test
def test_accepts_missing_data_field() -> None:
    meta = _valid_meta()
    del meta["data"]
    r = geofred_regional_data.Response.model_validate(_valid_response(meta=meta))
    assert r.meta.data is None


@pytest.mark.contract_test
def test_rejects_missing_meta() -> None:
    with pytest.raises(ValidationError):
        geofred_regional_data.Response.model_validate({})
