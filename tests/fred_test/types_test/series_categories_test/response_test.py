from pydantic import ValidationError
import pytest

from fred import series_categories


def _valid_category(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"id": 95, "name": "Monthly Rates", "parent_id": 15}
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"categories": [_valid_category()]}
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = series_categories.Response.model_validate(_valid_response())
    assert len(r.categories) == 1
    assert r.categories[0].id == 95


@pytest.mark.contract_test
def test_accepts_empty_categories() -> None:
    r = series_categories.Response.model_validate(_valid_response(categories=[]))
    assert r.categories == []


@pytest.mark.contract_test
def test_rejects_missing_categories() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["categories"]
        series_categories.Response.model_validate(data)
