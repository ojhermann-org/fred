from pydantic import ValidationError
import pytest

from fred import release_dates
from fred.enums import SortOrder
from fred.enums.order_by import ReleaseDates as OrderBy


def _valid_release_date(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "release_id": 82,
        "date": "1997-02-10",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "1776-07-04",
        "realtime_end": "9999-12-31",
        "order_by": "release_date",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 10000,
        "release_dates": [_valid_release_date()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = release_dates.Response.model_validate(_valid_response())
    assert r.realtime_start == "1776-07-04"
    assert r.realtime_end == "9999-12-31"
    assert r.order_by == OrderBy.release_date
    assert r.sort_order == SortOrder.asc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 10000
    assert len(r.release_dates) == 1


@pytest.mark.contract_test
def test_accepts_multiple_release_dates() -> None:
    r = release_dates.Response.model_validate(
        _valid_response(
            release_dates=[
                _valid_release_date(),
                _valid_release_date(date="1998-02-10"),
            ],
            count=2,
        )
    )
    assert len(r.release_dates) == 2
    assert r.release_dates[1].date == "1998-02-10"


@pytest.mark.contract_test
def test_accepts_empty_release_dates_list() -> None:
    r = release_dates.Response.model_validate(
        _valid_response(release_dates=[], count=0)
    )
    assert r.release_dates == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        release_dates.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_sort_order() -> None:
    with pytest.raises(ValidationError):
        release_dates.Response.model_validate(_valid_response(sort_order="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        release_dates.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_release_dates_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["release_dates"]
        release_dates.Response.model_validate(data)
