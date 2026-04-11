from pydantic import TypeAdapter, ValidationError
import pytest

from fred.types.limit import Limit

_adapter = TypeAdapter(Limit)


@pytest.mark.contract_test
def test_rejects_less_than_1() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(0)


@pytest.mark.contract_test
def test_accepts_1() -> None:
    assert _adapter.validate_python(1) == 1


@pytest.mark.contract_test
def test_accepts_mid_range_value() -> None:
    assert _adapter.validate_python(500) == 500


@pytest.mark.contract_test
def test_accepts_1000() -> None:
    assert _adapter.validate_python(1000) == 1000


@pytest.mark.contract_test
def test_rejects_greater_than_1000() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(1001)


@pytest.mark.contract_test
def test_rejects_float() -> None:
    with pytest.raises(ValidationError):
        _adapter.validate_python(1.5)
