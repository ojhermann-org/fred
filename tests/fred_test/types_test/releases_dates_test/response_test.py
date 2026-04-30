from pydantic import ValidationError
import pytest

from fred import releases_dates
from fred.enums import SortOrder
from fred.enums.order_by import ReleasesDates as OrderBy


def _valid_release_date(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "release_id": 9,
        "release_name": "Advance Monthly Sales for Retail and Food Services",
        "date": "2013-08-13",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-01-01",
        "realtime_end": "9999-12-31",
        "order_by": "release_date",
        "sort_order": "desc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "release_dates": [_valid_release_date()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = releases_dates.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-01-01"
    assert r.realtime_end == "9999-12-31"
    assert r.order_by == OrderBy.release_date
    assert r.sort_order == SortOrder.desc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 1000
    assert len(r.release_dates) == 1


@pytest.mark.contract_test
def test_accepts_multiple_release_dates() -> None:
    r = releases_dates.Response.model_validate(
        _valid_response(
            release_dates=[_valid_release_date(), _valid_release_date(release_id=10)],
            count=2,
        )
    )
    assert len(r.release_dates) == 2
    assert r.release_dates[1].release_id == 10


@pytest.mark.contract_test
def test_accepts_empty_release_dates_list() -> None:
    r = releases_dates.Response.model_validate(
        _valid_response(release_dates=[], count=0)
    )
    assert r.release_dates == []


@pytest.mark.contract_test
def test_order_by_parsed_as_enum() -> None:
    r = releases_dates.Response.model_validate(_valid_response(order_by="release_id"))
    assert r.order_by == OrderBy.release_id


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        releases_dates.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_sort_order() -> None:
    with pytest.raises(ValidationError):
        releases_dates.Response.model_validate(_valid_response(sort_order="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        releases_dates.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_release_dates_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["release_dates"]
        releases_dates.Response.model_validate(data)
