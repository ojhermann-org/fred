from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.category_request_params import CategoryRequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = CategoryRequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.category_id == 0


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        CategoryRequestParams(file_type=FileType.json, category_id=0)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        CategoryRequestParams(api_key=_VALID_API_KEY, category_id=0)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_category_id() -> None:
    with pytest.raises(ValidationError):
        CategoryRequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_negative_category_id() -> None:
    with pytest.raises(ValidationError):
        CategoryRequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=-1,
        )
