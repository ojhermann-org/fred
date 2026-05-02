from pydantic import ValidationError
import pytest

from fred.enums.shape import Shape
from fred.types.geofred_shapes.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, shape=Shape.bea)
    assert p.api_key == _VALID_API_KEY
    assert p.shape == Shape.bea


@pytest.mark.contract_test
def test_accepts_all_shapes() -> None:
    for shape in Shape:
        p = RequestParams(api_key=_VALID_API_KEY, shape=shape)
        assert p.shape == shape


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(shape=Shape.bea)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_shape() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_invalid_shape() -> None:
    with pytest.raises(ValidationError):
        RequestParams.model_validate({"api_key": _VALID_API_KEY, "shape": "invalid"})
