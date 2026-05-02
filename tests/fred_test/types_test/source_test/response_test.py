from pydantic import ValidationError
import pytest

from fred import source


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
        "sources": [_valid_source()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = source.Response.model_validate(_valid_response())
    assert len(r.sources) == 1
    assert r.sources[0].id == 1
    assert r.sources[0].name == "Board of Governors of the Federal Reserve System"


@pytest.mark.contract_test
def test_accepts_null_link() -> None:
    r = source.Response.model_validate(
        _valid_response(sources=[_valid_source(link=None)])
    )
    assert r.sources[0].link is None


@pytest.mark.contract_test
def test_accepts_notes() -> None:
    r = source.Response.model_validate(
        _valid_response(sources=[_valid_source(notes="IMF notes.")])
    )
    assert r.sources[0].notes == "IMF notes."


@pytest.mark.contract_test
def test_rejects_missing_sources() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["sources"]
        source.Response.model_validate(data)
