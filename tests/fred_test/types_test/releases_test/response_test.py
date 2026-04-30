from pydantic import ValidationError
import pytest

from fred import releases
from fred.enums import SortOrder
from fred.enums.order_by import Releases as OrderBy


def _valid_release(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 10,
        "realtime_start": "2013-08-13",
        "realtime_end": "2013-08-13",
        "name": "Consumer Price Index",
        "press_release": True,
        "link": "http://www.bls.gov/cpi/",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-13",
        "realtime_end": "2013-08-13",
        "order_by": "release_id",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "releases": [_valid_release()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = releases.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-13"
    assert r.realtime_end == "2013-08-13"
    assert r.order_by == OrderBy.release_id
    assert r.sort_order == SortOrder.asc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 1000
    assert len(r.releases) == 1


@pytest.mark.contract_test
def test_accepts_multiple_releases() -> None:
    r = releases.Response.model_validate(
        _valid_response(releases=[_valid_release(), _valid_release(id=11)], count=2)
    )
    assert len(r.releases) == 2
    assert r.releases[1].id == 11


@pytest.mark.contract_test
def test_accepts_empty_releases_list() -> None:
    r = releases.Response.model_validate(_valid_response(releases=[], count=0))
    assert r.releases == []


@pytest.mark.contract_test
def test_order_by_parsed_as_enum() -> None:
    r = releases.Response.model_validate(_valid_response(order_by="name"))
    assert r.order_by == OrderBy.name


@pytest.mark.contract_test
def test_release_with_no_link() -> None:
    r = releases.Response.model_validate(
        _valid_response(releases=[_valid_release(link=None)])
    )
    assert r.releases[0].link is None


@pytest.mark.contract_test
def test_release_with_notes() -> None:
    r = releases.Response.model_validate(
        _valid_response(releases=[_valid_release(notes="Some notes.")])
    )
    assert r.releases[0].notes == "Some notes."


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        releases.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_sort_order() -> None:
    with pytest.raises(ValidationError):
        releases.Response.model_validate(_valid_response(sort_order="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        releases.Response.model_validate(_valid_response(realtime_start="not-a-date"))


@pytest.mark.contract_test
def test_rejects_missing_releases_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["releases"]
        releases.Response.model_validate(data)
