from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.order_by import SeriesSearchRelatedTags as OrderBy
from fred.types.series_search_related_tags.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SEARCH_TEXT = "monetary service index"
_VALID_TAG_NAMES = "m2"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.series_search_text == _VALID_SEARCH_TEXT
    assert p.tag_names == _VALID_TAG_NAMES


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_search_text=_VALID_SEARCH_TEXT,
        tag_names=_VALID_TAG_NAMES,
        order_by=OrderBy.series_count,
    )
    assert p.order_by == OrderBy.series_count


@pytest.mark.contract_test
def test_rejects_missing_series_search_text() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
        )  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_search_text=_VALID_SEARCH_TEXT,
        )  # type: ignore[call-arg]
