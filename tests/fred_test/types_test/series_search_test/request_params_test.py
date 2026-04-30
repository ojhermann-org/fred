from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
import fred.enums.filter_variable as filter_variable
from fred.enums.order_by import SeriesSearch as OrderBy
from fred.enums.search_type import SearchType
from fred.enums.sort_order import SortOrder
from fred.types.series_search.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SEARCH_TEXT = "monetary service index"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.search_text == _VALID_SEARCH_TEXT


@pytest.mark.contract_test
def test_search_type_defaults_to_full_text() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.search_type == SearchType.full_text


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_filter_variable_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.filter_variable is None


@pytest.mark.contract_test
def test_accepts_explicit_filter_variable() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
        filter_variable=filter_variable.SeriesSearch.frequency,
    )
    assert p.filter_variable == filter_variable.SeriesSearch.frequency


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
        order_by=OrderBy.popularity,
    )
    assert p.order_by == OrderBy.popularity


@pytest.mark.contract_test
def test_rejects_missing_search_text() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.tag_names is None


@pytest.mark.contract_test
def test_exclude_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        search_text=_VALID_SEARCH_TEXT,
    )
    assert p.exclude_tag_names is None
