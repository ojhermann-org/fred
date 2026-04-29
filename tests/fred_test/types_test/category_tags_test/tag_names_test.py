from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.category_tags.tag_names import TagNames

_adapter = TypeAdapter(TagNames)


@pytest.mark.contract_test
def test_accepts_none() -> None:
    assert _adapter.validate_python(None) is None


@pytest.mark.contract_test
def test_rejects_empty_string() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("")


@pytest.mark.contract_test
def test_rejects_whitespace_only() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("   ")


@pytest.mark.contract_test
def test_accepts_single_string_no_semicolon() -> None:
    assert _adapter.validate_python("inflation") == "inflation"


@pytest.mark.contract_test
def test_rejects_colon_separated() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("inflation:gdp")


@pytest.mark.contract_test
def test_accepts_semicolon_separated() -> None:
    assert _adapter.validate_python("inflation;gdp") == "inflation;gdp"


@pytest.mark.contract_test
def test_rejects_semicolon_separated_with_whitespace() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("inflation; gdp")


@pytest.mark.contract_test
def test_rejects_leading_semicolon() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(";inflation")


@pytest.mark.contract_test
def test_rejects_trailing_semicolon() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("inflation;")


@pytest.mark.contract_test
def test_rejects_consecutive_semicolons() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("inflation;;gdp")
