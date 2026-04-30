from pydantic import ValidationError
import pytest

from fred.enums import SortOrder
from fred.enums.file_type import FileType
from fred.enums.order_by import ReleasesDates as OrderBy
from fred.types.releases_dates.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json


@pytest.mark.contract_test
def test_realtime_start_defaults_to_first_day_of_year() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.realtime_start.endswith("-01-01")


@pytest.mark.contract_test
def test_realtime_end_defaults_to_9999() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.realtime_end == "9999-12-31"


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_desc() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.sort_order == SortOrder.desc


@pytest.mark.contract_test
def test_include_release_dates_with_no_data_defaults_to_false() -> None:
    p = RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)
    assert p.include_release_dates_with_no_data is False


@pytest.mark.contract_test
def test_accepts_include_release_dates_with_no_data_true() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        include_release_dates_with_no_data=True,
    )
    assert p.include_release_dates_with_no_data is True


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, order_by=OrderBy.release_date
    )
    assert p.order_by == OrderBy.release_date


@pytest.mark.contract_test
def test_accepts_explicit_sort_order() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, sort_order=SortOrder.asc
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, limit=0)


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, limit=1001)


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, offset=-1)
