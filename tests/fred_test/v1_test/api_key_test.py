from pydantic import TypeAdapter, ValidationError
import pytest

from fred.v1.api_key import API_KEY

_adapter = TypeAdapter(API_KEY)

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"  # 32 lowercase alphanumeric chars


@pytest.mark.unit_test
def test_strips_whitespace() -> None:
    result = _adapter.validate_python(f"  {VALID_KEY}  ")
    assert result == VALID_KEY


@pytest.mark.unit_test
def test_rejects_key_shorter_than_32_chars() -> None:
    short_key = VALID_KEY[:-1]  # 31 chars
    with pytest.raises(ValidationError):
        _adapter.validate_python(short_key)


@pytest.mark.unit_test
def test_rejects_key_longer_than_32_chars() -> None:
    long_key = VALID_KEY + "a"  # 33 chars
    with pytest.raises(ValidationError):
        _adapter.validate_python(long_key)


@pytest.mark.unit_test
def test_rejects_uppercase_alpha() -> None:
    uppercase_key = VALID_KEY[:-1] + "A"  # replace last char with uppercase
    with pytest.raises(ValidationError):
        _adapter.validate_python(uppercase_key)


@pytest.mark.unit_test
def test_rejects_special_characters() -> None:
    special_key = VALID_KEY[:-1] + "-"  # replace last char with hyphen
    with pytest.raises(ValidationError):
        _adapter.validate_python(special_key)


@pytest.mark.unit_test
def test_rejects_empty_string() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("")


@pytest.mark.unit_test
def test_accepts_valid_key() -> None:
    result = _adapter.validate_python(VALID_KEY)
    assert result == VALID_KEY
