from pydantic import ValidationError
import pytest

from fred.types.release_dates.release_date import ReleaseDate


def _valid_release_date(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "release_id": 82,
        "date": "1997-02-10",
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_release_date() -> None:
    rd = ReleaseDate.model_validate(_valid_release_date())
    assert rd.release_id == 82
    assert rd.date == "1997-02-10"


@pytest.mark.contract_test
def test_rejects_invalid_date() -> None:
    with pytest.raises(ValidationError):
        ReleaseDate.model_validate(_valid_release_date(date="not-a-date"))


@pytest.mark.contract_test
def test_rejects_missing_release_id() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release_date()
        del data["release_id"]
        ReleaseDate.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_date() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release_date()
        del data["date"]
        ReleaseDate.model_validate(data)
