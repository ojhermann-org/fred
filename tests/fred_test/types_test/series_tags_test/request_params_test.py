from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.order_by import SeriesTags as OrderBy
from fred.enums.sort_order import SortOrder
from fred.types.series_tags.request_params import RequestParams

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
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
        order_by=OrderBy.series_count,
    )
    assert p.order_by == OrderBy.series_count


@pytest.mark.contract_test
def test_rejects_missing_series_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]
