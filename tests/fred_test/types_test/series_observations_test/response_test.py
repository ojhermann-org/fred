from pydantic import ValidationError
import pytest

from fred import series_observations
from fred.enums.output_type import OutputType
from fred.enums.sort_order import SortOrder


def _valid_observation(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "date": "2013-01-01",
        "value": "16577.3",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "observation_start": "1947-01-01",
        "observation_end": "2013-01-01",
        "units": "Billions of Chained 2009 Dollars",
        "output_type": 1,
        "file_type": "json",
        "order_by": "observation_date",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 100000,
        "observations": [_valid_observation()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = series_observations.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-14"
    assert r.output_type == OutputType.obs_by_real_time_period
    assert r.sort_order == SortOrder.asc
    assert len(r.observations) == 1


@pytest.mark.contract_test
def test_accepts_missing_value() -> None:
    r = series_observations.Response.model_validate(
        _valid_response(observations=[_valid_observation(value=".")])
    )
    assert r.observations[0].value == "."


@pytest.mark.contract_test
def test_accepts_empty_observations() -> None:
    r = series_observations.Response.model_validate(
        _valid_response(observations=[], count=0)
    )
    assert r.observations == []


@pytest.mark.contract_test
def test_rejects_missing_observations() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["observations"]
        series_observations.Response.model_validate(data)
