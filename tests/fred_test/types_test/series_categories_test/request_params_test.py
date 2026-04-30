from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.series_categories.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SERIES_ID = "GNPCA"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
    )
    assert p.series_id == _VALID_SERIES_ID


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_rejects_missing_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_empty_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, series_id="")
