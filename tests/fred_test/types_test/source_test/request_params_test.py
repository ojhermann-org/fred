from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.source.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SOURCE_ID = 1


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        source_id=_VALID_SOURCE_ID,
    )
    assert p.source_id == _VALID_SOURCE_ID


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json, source_id=_VALID_SOURCE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, source_id=_VALID_SOURCE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_source_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_source_id_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, source_id=0)
