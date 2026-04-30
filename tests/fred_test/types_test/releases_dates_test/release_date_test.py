from pydantic import ValidationError
import pytest

from fred.types.releases_dates.release_date import ReleaseDate


def _valid_release_date(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "release_id": 9,
        "release_name": "Advance Monthly Sales for Retail and Food Services",
        "date": "2013-08-13",
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_release_date() -> None:
    rd = ReleaseDate.model_validate(_valid_release_date())
    assert rd.release_id == 9
    assert rd.release_name == "Advance Monthly Sales for Retail and Food Services"
    assert rd.date == "2013-08-13"


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
def test_rejects_missing_release_name() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release_date()
        del data["release_name"]
        ReleaseDate.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_date() -> None:
    with pytest.raises(ValidationError):
        data = _valid_release_date()
        del data["date"]
        ReleaseDate.model_validate(data)
