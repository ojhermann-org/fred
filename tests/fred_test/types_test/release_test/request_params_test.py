from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.release.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_RELEASE_ID = 53


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.release_id == _VALID_RELEASE_ID


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_release_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_release_id_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, release_id=0)


@pytest.mark.contract_test
def test_rejects_negative_release_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, release_id=-1)
