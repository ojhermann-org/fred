from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.filter_value import SeriesUpdates as FilterValue
from fred.types.series_updates.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.api_key == _VALID_API_KEY


@pytest.mark.contract_test
def test_filter_value_defaults_to_all() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.filter_value == FilterValue.all


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.offset == 0


@pytest.mark.contract_test
def test_start_time_defaults_to_none() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.start_time is None


@pytest.mark.contract_test
def test_end_time_defaults_to_none() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.end_time is None


@pytest.mark.contract_test
def test_accepts_macro_filter_value() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        filter_value=FilterValue.macro,
    )
    assert p.filter_value == FilterValue.macro


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json)  # type: ignore[call-arg]
