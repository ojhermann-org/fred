from pydantic import ValidationError
import pytest

from fred import category


@pytest.mark.contract_test
def test_accepts_valid_category() -> None:
    c = category.Category(id=0, name="Categories", parent_id=0)
    assert c.id == 0
    assert c.name == "Categories"
    assert c.parent_id == 0


@pytest.mark.contract_test
def test_accepts_nonzero_ids() -> None:
    c = category.Category(
        id=13, name="Population, Employment, & Labor Markets", parent_id=1
    )
    assert c.id == 13
    assert c.parent_id == 1


@pytest.mark.contract_test
def test_rejects_negative_id() -> None:
    with pytest.raises(ValidationError):
        category.Category(id=-1, name="Invalid", parent_id=0)


@pytest.mark.contract_test
def test_rejects_negative_parent_id() -> None:
    with pytest.raises(ValidationError):
        category.Category(id=0, name="Invalid", parent_id=-1)


@pytest.mark.contract_test
def test_rejects_missing_id() -> None:
    with pytest.raises(ValidationError):
        category.Category(name="No ID", parent_id=0)  # ty: ignore[missing-argument]


@pytest.mark.contract_test
def test_rejects_missing_name() -> None:
    with pytest.raises(ValidationError):
        category.Category(id=0, parent_id=0)  # ty: ignore[missing-argument]


@pytest.mark.contract_test
def test_rejects_missing_parent_id() -> None:
    with pytest.raises(ValidationError):
        category.Category(id=0, name="No Parent")  # ty: ignore[missing-argument]
