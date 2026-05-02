from pydantic import ValidationError
import pytest

from fred.enums import SortOrder, TagGroupID
from fred.enums.file_type import FileType
from fred.enums.order_by import ReleaseRelatedTags as OrderBy
from fred.types.release_related_tags.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_RELEASE_ID = 86
_VALID_TAG_NAMES = "sa;foreign"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.release_id == _VALID_RELEASE_ID
    assert p.tag_names == _VALID_TAG_NAMES


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_exclude_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.exclude_tag_names is None


@pytest.mark.contract_test
def test_accepts_exclude_tag_names() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
        exclude_tag_names="monthly;financial",
    )
    assert p.exclude_tag_names == "monthly;financial"


@pytest.mark.contract_test
def test_rejects_invalid_exclude_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
            exclude_tag_names="monthly;",
        )


@pytest.mark.contract_test
def test_tag_group_id_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.tag_group_id is None


@pytest.mark.contract_test
def test_accepts_explicit_tag_group_id() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
        tag_group_id=TagGroupID.gen,
    )
    assert p.tag_group_id == TagGroupID.gen


@pytest.mark.contract_test
def test_search_text_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.search_text is None


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
        order_by=OrderBy.popularity,
    )
    assert p.order_by == OrderBy.popularity


@pytest.mark.contract_test
def test_accepts_explicit_sort_order() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names=_VALID_TAG_NAMES,
        sort_order=SortOrder.desc,
    )
    assert p.sort_order == SortOrder.desc


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
        )


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
        )


@pytest.mark.contract_test
def test_rejects_missing_release_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            tag_names=_VALID_TAG_NAMES,
        )


@pytest.mark.contract_test
def test_rejects_missing_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
        )


@pytest.mark.contract_test
def test_rejects_invalid_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names="inflation;",
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
            limit=1001,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names=_VALID_TAG_NAMES,
            offset=-1,
        )
