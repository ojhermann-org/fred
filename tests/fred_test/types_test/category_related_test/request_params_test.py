from pydantic import ValidationError
import pytest

from fred import category_related

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = category_related.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category_related.FileType.json,
        category_id=0,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == category_related.FileType.json
    assert p.category_id == 0


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = category_related.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category_related.FileType.json,
        category_id=0,
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = category_related.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category_related.FileType.json,
        category_id=0,
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_accepts_explicit_realtime_start() -> None:
    p = category_related.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category_related.FileType.json,
        category_id=0,
        realtime_start="2020-01-01",
    )
    assert p.realtime_start == "2020-01-01"


@pytest.mark.contract_test
def test_accepts_explicit_realtime_end() -> None:
    p = category_related.RequestParams(
        api_key=_VALID_API_KEY,
        file_type=category_related.FileType.json,
        category_id=0,
        realtime_end="2024-12-31",
    )
    assert p.realtime_end == "2024-12-31"


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        category_related.RequestParams(  # type: ignore[call-arg]
            file_type=category_related.FileType.json,
            category_id=0,
        )


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        category_related.RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            category_id=0,
        )


@pytest.mark.contract_test
def test_rejects_missing_category_id() -> None:
    with pytest.raises(ValidationError):
        category_related.RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=category_related.FileType.json,
        )


@pytest.mark.contract_test
def test_rejects_negative_category_id() -> None:
    with pytest.raises(ValidationError):
        category_related.RequestParams(
            api_key=_VALID_API_KEY,
            file_type=category_related.FileType.json,
            category_id=-1,
        )
