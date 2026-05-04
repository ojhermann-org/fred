from pydantic import ValidationError
import pytest

from fred import geofred_series_group


def _valid_series_group(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "title": "All Employees: Total Private",
        "region_type": "state",
        "series_group": "1223",
        "season": "NSA",
        "units": "Thousands of Persons",
        "frequency": "Annual",
        "min_date": "1990-01-01",
        "max_date": "2021-01-01",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"series_group": _valid_series_group()}
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = geofred_series_group.Response.model_validate(_valid_response())
    assert r.series_group.title == "All Employees: Total Private"
    assert r.series_group.region_type == "state"
    assert r.series_group.series_group == "1223"
    assert r.series_group.season == "NSA"
    assert r.series_group.units == "Thousands of Persons"
    assert r.series_group.frequency == "Annual"
    assert r.series_group.min_date == "1990-01-01"
    assert r.series_group.max_date == "2021-01-01"


@pytest.mark.contract_test
def test_rejects_missing_series_group() -> None:
    with pytest.raises(ValidationError):
        geofred_series_group.Response.model_validate({})


@pytest.mark.contract_test
def test_rejects_missing_title() -> None:
    sg = _valid_series_group()
    del sg["title"]
    with pytest.raises(ValidationError):
        geofred_series_group.Response.model_validate(_valid_response(series_group=sg))


@pytest.mark.contract_test
def test_rejects_invalid_min_date() -> None:
    with pytest.raises(ValidationError):
        geofred_series_group.Response.model_validate(
            _valid_response(series_group=_valid_series_group(min_date="not-a-date"))
        )


@pytest.mark.contract_test
def test_rejects_invalid_max_date() -> None:
    with pytest.raises(ValidationError):
        geofred_series_group.Response.model_validate(
            _valid_response(series_group=_valid_series_group(max_date="not-a-date"))
        )
