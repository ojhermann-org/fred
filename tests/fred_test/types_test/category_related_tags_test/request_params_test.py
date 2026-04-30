from pydantic import ValidationError
import pytest

from fred.enums import SortOrder, TagGroupID
from fred.enums.file_type import FileType
from fred.enums.order_by import CategoryRelatedTags as OrderBy
from fred.types.category_related_tags.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services;quarterly",
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.category_id == 125
    assert p.tag_names == "services;quarterly"


@pytest.mark.contract_test
def test_tag_names_is_required() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=125,
        )


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_exclude_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.exclude_tag_names is None


@pytest.mark.contract_test
def test_accepts_exclude_tag_names() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
        exclude_tag_names="goods;sa",
    )
    assert p.exclude_tag_names == "goods;sa"


@pytest.mark.contract_test
def test_rejects_invalid_exclude_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=125,
            tag_names="services",
            exclude_tag_names="goods sa",
        )


@pytest.mark.contract_test
def test_tag_group_id_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.tag_group_id is None


@pytest.mark.contract_test
def test_accepts_explicit_tag_group_id() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
        tag_group_id=TagGroupID.geo,
    )
    assert p.tag_group_id == TagGroupID.geo


@pytest.mark.contract_test
def test_search_text_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.search_text is None


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
        order_by=OrderBy.series_count,
    )
    assert p.order_by == OrderBy.series_count


@pytest.mark.contract_test
def test_accepts_explicit_sort_order() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=125,
        tag_names="services",
        sort_order=SortOrder.desc,
    )
    assert p.sort_order == SortOrder.desc


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            file_type=FileType.json,
            category_id=125,
            tag_names="services",
        )


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            category_id=125,
            tag_names="services",
        )


@pytest.mark.contract_test
def test_rejects_missing_category_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            tag_names="services",
        )


@pytest.mark.contract_test
def test_rejects_negative_category_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=-1,
            tag_names="services",
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=125,
            tag_names="services",
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=125,
            tag_names="services",
            limit=1001,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=125,
            tag_names="services",
            offset=-1,
        )
