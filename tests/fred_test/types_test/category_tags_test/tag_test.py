from pydantic import ValidationError
import pytest

from fred.types.category_tags.tag import Tag


def _valid_tag(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "bea",
        "group_id": "src",
        "notes": "U.S. Department of Commerce: Bureau of Economic Analysis",
        "created": "2012-02-27 10:18:19-06",
        "popularity": 87,
        "series_count": 24,
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_tag() -> None:
    t = Tag.model_validate(_valid_tag())
    assert t.name == "bea"
    assert t.group_id == "src"
    assert t.notes == "U.S. Department of Commerce: Bureau of Economic Analysis"
    assert t.created == "2012-02-27 10:18:19-06"
    assert t.popularity == 87
    assert t.series_count == 24


@pytest.mark.contract_test
def test_accepts_unknown_group_id() -> None:
    t = Tag.model_validate(_valid_tag(group_id="cc"))
    assert t.group_id == "cc"


@pytest.mark.contract_test
def test_accepts_empty_notes() -> None:
    t = Tag.model_validate(_valid_tag(notes=""))
    assert t.notes == ""


@pytest.mark.contract_test
def test_accepts_none_notes() -> None:
    t = Tag.model_validate(_valid_tag(notes=None))
    assert t.notes is None


@pytest.mark.contract_test
def test_rejects_invalid_created_format() -> None:
    with pytest.raises(ValidationError):
        Tag.model_validate(_valid_tag(created="2012-02-27"))


@pytest.mark.contract_test
def test_rejects_missing_name() -> None:
    with pytest.raises(ValidationError):
        data = _valid_tag()
        del data["name"]
        Tag.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_group_id() -> None:
    with pytest.raises(ValidationError):
        data = _valid_tag()
        del data["group_id"]
        Tag.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_created() -> None:
    with pytest.raises(ValidationError):
        data = _valid_tag()
        del data["created"]
        Tag.model_validate(data)
