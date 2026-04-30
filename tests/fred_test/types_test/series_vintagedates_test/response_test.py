from pydantic import ValidationError
import pytest

from fred import series_vintagedates
from fred.enums.sort_order import SortOrder


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "1776-07-04",
        "realtime_end": "9999-12-31",
        "order_by": "vintage_date",
        "sort_order": "asc",
        "count": 2,
        "offset": 0,
        "limit": 10000,
        "vintage_dates": ["1958-12-21", "1959-02-19"],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = series_vintagedates.Response.model_validate(_valid_response())
    assert r.sort_order == SortOrder.asc
    assert len(r.vintage_dates) == 2
    assert r.vintage_dates[0] == "1958-12-21"


@pytest.mark.contract_test
def test_accepts_empty_vintage_dates() -> None:
    r = series_vintagedates.Response.model_validate(
        _valid_response(vintage_dates=[], count=0)
    )
    assert r.vintage_dates == []


@pytest.mark.contract_test
def test_rejects_missing_vintage_dates() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["vintage_dates"]
        series_vintagedates.Response.model_validate(data)
