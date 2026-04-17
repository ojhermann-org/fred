from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.offset import Offset

_adapter = TypeAdapter(Offset)


@pytest.mark.contract_test
def test_rejects_negative_int() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(-1)


@pytest.mark.contract_test
def test_accepts_zero() -> None:
    assert _adapter.validate_python(0) == 0


@pytest.mark.contract_test
def test_accepts_positive_int() -> None:
    assert _adapter.validate_python(42) == 42


@pytest.mark.contract_test
def test_rejects_float() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(1.5)
