from pydantic import ValidationError
import pytest

from fred import release_sources


def _valid_source(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 18,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "U.S. Department of Commerce: Bureau of Economic Analysis",
        "link": "http://www.bea.gov/",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "sources": [_valid_source()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = release_sources.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-14"
    assert r.realtime_end == "2013-08-14"
    assert len(r.sources) == 1
    assert r.sources[0].id == 18
    assert (
        r.sources[0].name == "U.S. Department of Commerce: Bureau of Economic Analysis"
    )
    assert r.sources[0].link == "http://www.bea.gov/"


@pytest.mark.contract_test
def test_accepts_multiple_sources() -> None:
    r = release_sources.Response.model_validate(
        _valid_response(sources=[_valid_source(), _valid_source(id=19)])
    )
    assert len(r.sources) == 2
    assert r.sources[1].id == 19


@pytest.mark.contract_test
def test_accepts_empty_sources_list() -> None:
    r = release_sources.Response.model_validate(_valid_response(sources=[]))
    assert r.sources == []


@pytest.mark.contract_test
def test_source_link_can_be_none() -> None:
    r = release_sources.Response.model_validate(
        _valid_response(sources=[_valid_source(link=None)])
    )
    assert r.sources[0].link is None


@pytest.mark.contract_test
def test_source_notes_can_be_none() -> None:
    r = release_sources.Response.model_validate(
        _valid_response(sources=[_valid_source(notes=None)])
    )
    assert r.sources[0].notes is None


@pytest.mark.contract_test
def test_source_accepts_notes() -> None:
    r = release_sources.Response.model_validate(
        _valid_response(sources=[_valid_source(notes="Some notes.")])
    )
    assert r.sources[0].notes == "Some notes."


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        release_sources.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_sources_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["sources"]
        release_sources.Response.model_validate(data)
