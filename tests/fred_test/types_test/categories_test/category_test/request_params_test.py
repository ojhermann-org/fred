from pydantic import ValidationError
import pytest

from fred import category

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = category.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category.FileType.json,
        category_id=0,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == category.FileType.json
    assert p.category_id == 0


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        category.RequestParams(file_type=category.FileType.json, category_id=0)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        category.RequestParams(api_key=_VALID_API_KEY, category_id=0)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_category_id() -> None:
    with pytest.raises(ValidationError):
        category.RequestParams(api_key=_VALID_API_KEY, file_type=category.FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_negative_category_id() -> None:
    with pytest.raises(ValidationError):
        category.RequestParams(
            api_key=_VALID_API_KEY,
            file_type=category.FileType.json,
            category_id=-1,
        )
