from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.fred_timestamp import FredTimestamp

_adapter = TypeAdapter(FredTimestamp)


@pytest.mark.contract_test
def test_accepts_valid_value() -> None:
    assert (
        _adapter.validate_python("2017-07-06 09:32:14-05") == "2017-07-06 09:32:14-05"
    )


@pytest.mark.contract_test
def test_accepts_valid_value_with_positive_offset() -> None:
    assert (
        _adapter.validate_python("2017-07-06 09:32:14+05") == "2017-07-06 09:32:14+05"
    )


@pytest.mark.contract_test
def test_accepts_valid_value_with_strippable_whitespace() -> None:
    assert (
        _adapter.validate_python("  2017-07-06 09:32:14-05  ")
        == "2017-07-06 09:32:14-05"
    )


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
        "2017-07-06",  # date only, no time
        "2017-07-06 09:32:14",  # no timezone offset
        "2017-07-06T09:32:14-05",  # T separator instead of space
        "2017-13-06 09:32:14-05",  # invalid month
        "2017-07-06 25:32:14-05",  # invalid hour
        "2017-07-06 09:32:14-15",  # invalid offset hour
        "2017/07/06 09:32:14-05",  # slashes in date
        "not-a-datetime",
    ],
)
def test_rejects_invalid_formats(value: str) -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(value)


@pytest.mark.contract_test
def test_rejects_impossible_date() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python("2024-02-30 09:32:14-05")
