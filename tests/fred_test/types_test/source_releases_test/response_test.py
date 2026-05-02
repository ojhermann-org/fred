from pydantic import ValidationError
import pytest

from fred import source_releases
from fred.enums.order_by import SourceReleases as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_release(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 13,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "G.17 Industrial Production and Capacity Utilization",
        "press_release": True,
        "link": "http://www.federalreserve.gov/releases/g17/",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
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
    r = source_releases.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.release_id
    assert r.sort_order == SortOrder.asc
    assert len(r.releases) == 1
    assert r.releases[0].id == 13


@pytest.mark.contract_test
def test_accepts_null_link() -> None:
    r = source_releases.Response.model_validate(
        _valid_response(releases=[_valid_release(link=None)])
    )
    assert r.releases[0].link is None


@pytest.mark.contract_test
def test_accepts_notes() -> None:
    r = source_releases.Response.model_validate(
        _valid_response(releases=[_valid_release(notes="Some notes.")])
    )
    assert r.releases[0].notes == "Some notes."


@pytest.mark.contract_test
def test_accepts_empty_releases() -> None:
    r = source_releases.Response.model_validate(_valid_response(releases=[], count=0))
    assert r.releases == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        source_releases.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_missing_releases() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["releases"]
        source_releases.Response.model_validate(data)
