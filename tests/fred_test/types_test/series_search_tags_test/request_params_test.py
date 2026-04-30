from pydantic import ValidationError
import pytest

from fred.enums import TagGroupID
from fred.enums.file_type import FileType
from fred.enums.order_by import SeriesSearchTags as OrderBy
from fred.enums.search_type import SearchType
from fred.types.series_search_tags.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SEARCH_TEXT = "monetary service index"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
    )
    assert p.series_search_text == _VALID_SEARCH_TEXT


@pytest.mark.contract_test
def test_search_type_defaults_to_full_text() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
    )
    assert p.search_type == SearchType.full_text


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_tag_group_id_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
    )
    assert p.tag_group_id is None


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        order_by=OrderBy.series_count,
    )
    assert p.order_by == OrderBy.series_count


@pytest.mark.contract_test
def test_accepts_explicit_tag_group_id() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        tag_group_id=TagGroupID.freq,
    )
    assert p.tag_group_id == TagGroupID.freq


@pytest.mark.contract_test
def test_rejects_missing_series_search_text() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]
