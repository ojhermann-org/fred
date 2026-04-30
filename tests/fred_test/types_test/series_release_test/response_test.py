from pydantic import ValidationError
import pytest

from fred import series_release


def _valid_release(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": 21,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "Gross National Product",
        "press_release": True,
        "link": "http://www.bea.gov/national/index.htm",
        "notes": None,
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
    r = series_release.Response.model_validate(_valid_response())
    assert len(r.releases) == 1
    assert r.releases[0].id == 21
    assert r.releases[0].press_release is True


@pytest.mark.contract_test
def test_accepts_null_link() -> None:
    r = series_release.Response.model_validate(
        _valid_response(releases=[_valid_release(link=None)])
    )
    assert r.releases[0].link is None


@pytest.mark.contract_test
def test_rejects_missing_releases() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["releases"]
        series_release.Response.model_validate(data)
