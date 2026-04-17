from pydantic import ValidationError
import pytest

from fred import category


@pytest.mark.contract_test
def test_accepts_single_category() -> None:
    r = category.Response(categories=[{"id": 0, "name": "Categories", "parent_id": 0}])  # ty: ignore[invalid-argument-type]
    assert len(r.categories) == 1
    assert r.categories[0].id == 0
    assert r.categories[0].name == "Categories"
    assert r.categories[0].parent_id == 0


@pytest.mark.contract_test
def test_accepts_multiple_categories() -> None:
    r = category.Response(
        categories=[  # ty: ignore[invalid-argument-type]
            {"id": 0, "name": "Categories", "parent_id": 0},
            {
                "id": 13,
                "name": "Population, Employment, & Labor Markets",
                "parent_id": 1,
            },
        ]
    )
    assert len(r.categories) == 2
    assert r.categories[1].id == 13


@pytest.mark.contract_test
def test_accepts_empty_list() -> None:
    r = category.Response(categories=[])
    assert r.categories == []


@pytest.mark.contract_test
def test_rejects_category_with_negative_id() -> None:
    with pytest.raises(ValidationError):
        category.Response(categories=[{"id": -1, "name": "Bad", "parent_id": 0}])  # ty: ignore[invalid-argument-type]


@pytest.mark.contract_test
def test_rejects_missing_categories_field() -> None:
    with pytest.raises(ValidationError):
        category.Response()  # ty: ignore[missing-argument]
