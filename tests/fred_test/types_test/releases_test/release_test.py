from pydantic import ValidationError
import pytest

from fred.types.releases.release import Release


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


@pytest.mark.contract_test
def test_accepts_valid_release() -> None:
    r = Release.model_validate(_valid_release())
    assert r.id == 10
    assert r.realtime_start == "2013-08-13"
    assert r.realtime_end == "2013-08-13"
    assert r.name == "Consumer Price Index"
    assert r.press_release is True
    assert r.link == "http://www.bls.gov/cpi/"
    assert r.notes is None


@pytest.mark.contract_test
def test_accepts_none_link() -> None:
    r = Release.model_validate(_valid_release(link=None))
    assert r.link is None


@pytest.mark.contract_test
def test_link_defaults_to_none_when_absent() -> None:
    data = _valid_release()
    del data["link"]
    r = Release.model_validate(data)
    assert r.link is None


@pytest.mark.contract_test
def test_accepts_notes() -> None:
    r = Release.model_validate(_valid_release(notes="Some notes."))
    assert r.notes == "Some notes."


@pytest.mark.contract_test
def test_notes_defaults_to_none_when_absent() -> None:
    r = Release.model_validate(_valid_release())
    assert r.notes is None


@pytest.mark.contract_test
def test_press_release_false() -> None:
    r = Release.model_validate(_valid_release(press_release=False))
    assert r.press_release is False


@pytest.mark.contract_test
def test_rejects_missing_id() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release()
        del data["id"]
        Release.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_name() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release()
        del data["name"]
        Release.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        Release.model_validate(_valid_release(realtime_start="not-a-date"))
