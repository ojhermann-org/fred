from pydantic import TypeAdapter, ValidationError
import pytest

from fred.request.implementation.realtime import Realtime

_adapter = TypeAdapter(Realtime)


@pytest.mark.unit_test
def test_raises_on_empty_string() -> None:
    with pytest.raises(ValidationError, match="Value cannot be empty"):
        _adapter.validate_python("")


@pytest.mark.unit_test
def test_raises_on_only_whitespace() -> None:
    with pytest.raises(ValidationError, match="Value cannot be empty"):
        _adapter.validate_python("    ")


@pytest.mark.unit_test
@pytest.mark.parametrize(
    "value",
    [
        "01-01-2024",  # DD-MM-YYYY
        "2024/01/15",  # slashes
        "20240115",  # no separators
        "2024-13-01",  # invalid month
        "2024-01-32",  # invalid day
        "not-a-date",
    ],
)
def test_raises_on_wrong_formats(value: str) -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(value)


@pytest.mark.unit_test
def test_accepts_valid_isoformat_date() -> None:
    result = _adapter.validate_python("2024-01-15")
    assert result == "2024-01-15"


@pytest.mark.unit_test
def test_strips_whitespace() -> None:
    result = _adapter.validate_python("  2024-01-15  ")
    assert result == "2024-01-15"
