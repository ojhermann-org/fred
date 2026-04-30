from pydantic import ValidationError
import pytest

from fred import release


def _valid_release(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 53,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "Gross Domestic Product",
        "press_release": True,
        "link": "http://www.bea.gov/national/index.htm",
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "releases": [_valid_release()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = release.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-14"
    assert r.realtime_end == "2013-08-14"
    assert len(r.releases) == 1
    assert r.releases[0].id == 53
    assert r.releases[0].name == "Gross Domestic Product"
    assert r.releases[0].press_release is True


@pytest.mark.contract_test
def test_accepts_release_with_no_link() -> None:
    r = release.Response.model_validate(
        _valid_response(releases=[_valid_release(link=None)])
    )
    assert r.releases[0].link is None


@pytest.mark.contract_test
def test_accepts_release_with_notes() -> None:
    r = release.Response.model_validate(
        _valid_response(releases=[_valid_release(notes="Some notes.")])
    )
    assert r.releases[0].notes == "Some notes."


@pytest.mark.contract_test
def test_accepts_empty_releases_list() -> None:
    r = release.Response.model_validate(_valid_response(releases=[]))
    assert r.releases == []


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        release.Response.model_validate(_valid_response(realtime_start="not-a-date"))


@pytest.mark.contract_test
def test_rejects_missing_releases_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["releases"]
        release.Response.model_validate(data)
