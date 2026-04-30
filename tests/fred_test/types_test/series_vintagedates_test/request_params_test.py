from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.sort_order import SortOrder
from fred.types.series_vintagedates.request_params import RequestParams

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
def test_limit_defaults_to_10000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.limit == 10000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_rejects_limit_above_10000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            limit=10001,
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_missing_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]
