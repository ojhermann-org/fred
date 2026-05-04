from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.geofred_series_data.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SERIES_ID = "WIPCPI"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.series_id == _VALID_SERIES_ID
    assert p.date is None
    assert p.start_date is None


@pytest.mark.contract_test
def test_accepts_date() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
        date="2012-01-01",
    )
    assert p.date == "2012-01-01"


@pytest.mark.contract_test
def test_accepts_start_date() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
        start_date="2010-01-01",
    )
    assert p.start_date == "2010-01-01"


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json, series_id=_VALID_SERIES_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, series_id=_VALID_SERIES_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_empty_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, series_id="")


@pytest.mark.contract_test
def test_rejects_invalid_date() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            date="not-a-date",
        )


@pytest.mark.contract_test
def test_rejects_invalid_start_date() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            start_date="not-a-date",
        )
