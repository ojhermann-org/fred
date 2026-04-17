from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.api_key import ApiKey

_adapter = TypeAdapter(ApiKey)

_VALID = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_value() -> None:
    assert _adapter.validate_python(_VALID) == _VALID


@pytest.mark.contract_test
def test_rejects_uppercase() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(_VALID.upper())


@pytest.mark.contract_test
@pytest.mark.parametrize(
    "value",
    [
        "abcdefghijklmnopqrstuvwxyz01234-",  # hyphen
        "abcdefghijklmnopqrstuvwxyz01234:",  # colon
        "abcdefghijklmnopqrstuvwxyz01234_",  # underscore
    ],
)
def test_rejects_non_alphanumeric(value: str) -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(value)


@pytest.mark.contract_test
def test_rejects_one_alpha_removed() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("bcdefghijklmnopqrstuvwxyz012345")


@pytest.mark.contract_test
def test_rejects_one_numeric_removed() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("abcdefghijklmnopqrstuvwxyz01234")


@pytest.mark.contract_test
def test_rejects_one_alpha_added() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("aabcdefghijklmnopqrstuvwxyz012345")


@pytest.mark.contract_test
def test_rejects_one_numeric_added() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("abcdefghijklmnopqrstuvwxyz0123456")


@pytest.mark.contract_test
def test_accepts_valid_value_with_strippable_whitespace() -> None:
    assert _adapter.validate_python(f"  {_VALID}  ") == _VALID
