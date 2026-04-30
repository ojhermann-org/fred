from typing import Optional

from pydantic import BaseModel
import pytest

from fred.functions.for_request import for_request


class _AllStrings(BaseModel):
    a: str
    b: str


class _WithOptional(BaseModel):
    a: str
    b: Optional[str] = None


class _WithInt(BaseModel):
    a: int
    b: str


class _WithBool(BaseModel):
    a: bool
    b: str


@pytest.mark.unit_test
def test_returns_all_fields_as_strings() -> None:
    assert for_request(_AllStrings(a="x", b="y")) == {"a": "x", "b": "y"}


@pytest.mark.unit_test
def test_excludes_none_fields() -> None:
    assert for_request(_WithOptional(a="x")) == {"a": "x"}


@pytest.mark.unit_test
def test_includes_non_none_optional_fields() -> None:
    assert for_request(_WithOptional(a="x", b="y")) == {"a": "x", "b": "y"}


@pytest.mark.unit_test
def test_converts_non_string_values_to_strings() -> None:
    assert for_request(_WithInt(a=42, b="z")) == {"a": "42", "b": "z"}


@pytest.mark.unit_test
def test_converts_true_to_lowercase_string() -> None:
    assert for_request(_WithBool(a=True, b="z")) == {"a": "true", "b": "z"}


@pytest.mark.unit_test
def test_converts_false_to_lowercase_string() -> None:
    assert for_request(_WithBool(a=False, b="z")) == {"a": "false", "b": "z"}


@pytest.mark.unit_test
def test_empty_model_returns_empty_dict() -> None:
    class _Empty(BaseModel):
        pass

    assert for_request(_Empty()) == {}
