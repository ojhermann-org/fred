from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.order_by import RelatedTags as OrderBy
from fred.enums.sort_order import SortOrder
from fred.types.tags_related.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_TAG_NAMES = "monetary+aggregates;weekly"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.api_key == _VALID_API_KEY
    assert p.tag_names == _VALID_TAG_NAMES


@pytest.mark.contract_test
def test_exclude_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.exclude_tag_names is None


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, tag_names=_VALID_TAG_NAMES
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        tag_names=_VALID_TAG_NAMES,
        order_by=OrderBy.name,
    )
    assert p.order_by == OrderBy.name


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            file_type=FileType.json, tag_names=_VALID_TAG_NAMES
        )


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY, tag_names=_VALID_TAG_NAMES
        )


@pytest.mark.contract_test
def test_rejects_missing_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY, file_type=FileType.json
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            tag_names=_VALID_TAG_NAMES,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            tag_names=_VALID_TAG_NAMES,
            offset=-1,
        )
