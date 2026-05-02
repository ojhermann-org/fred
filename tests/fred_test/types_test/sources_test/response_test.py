from pydantic import ValidationError
import pytest

from fred import sources
from fred.enums.order_by import Sources as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_source(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 1,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "Board of Governors of the Federal Reserve System",
        "link": "http://www.federalreserve.gov/",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "order_by": "source_id",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "sources": [_valid_source()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = sources.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.source_id
    assert r.sort_order == SortOrder.asc
    assert len(r.sources) == 1
    assert r.sources[0].id == 1


@pytest.mark.contract_test
def test_accepts_null_link() -> None:
    r = sources.Response.model_validate(
        _valid_response(sources=[_valid_source(link=None)])
    )
    assert r.sources[0].link is None


@pytest.mark.contract_test
def test_accepts_notes() -> None:
    r = sources.Response.model_validate(
        _valid_response(sources=[_valid_source(notes="Some notes.")])
    )
    assert r.sources[0].notes == "Some notes."


@pytest.mark.contract_test
def test_accepts_empty_sources() -> None:
    r = sources.Response.model_validate(_valid_response(sources=[], count=0))
    assert r.sources == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        sources.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_missing_sources() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["sources"]
        sources.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        sources.Response.model_validate(_valid_response(realtime_start="not-a-date"))
