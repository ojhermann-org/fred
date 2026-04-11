from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.realtime import Realtime

_adapter = TypeAdapter(Realtime)


@pytest.mark.contract_test
def test_accepts_valid_value() -> None:
    assert _adapter.validate_python("2024-01-15") == "2024-01-15"


@pytest.mark.contract_test
def test_accepts_valid_value_with_strippable_whitespace() -> None:
    assert _adapter.validate_python("  2024-01-15  ") == "2024-01-15"


@pytest.mark.contract_test
def test_rejects_empty_string() -> None:
    with pytest.raises(ValidationError, match="Value cannot be empty"):
        _adapter.validate_python("")


@pytest.mark.contract_test
def test_rejects_whitespace_string() -> None:
    with pytest.raises(ValidationError, match="Value cannot be empty"):
        _adapter.validate_python("   ")


@pytest.mark.contract_test
@pytest.mark.parametrize(
    "value",
    [
        "01-15-2024",  # MM-DD-YYYY
        "2024/01/15",  # slashes
        "20240115",  # no separators
        "2024-13-01",  # invalid month
        "2024-01-32",  # invalid day
        "not-a-date",
    ],
)
def test_rejects_invalid_formats(value: str) -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(value)


@pytest.mark.contract_test
def test_rejects_impossible_date() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("2024-02-30")
