from pydantic import ValidationError
import pytest

from fred.enums import SortOrder, TagGroupID
from fred.enums.file_type import FileType
from fred.enums.order_by import ReleaseTags as OrderBy
from fred.types.release_tags.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_RELEASE_ID = 86


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.release_id == _VALID_RELEASE_ID


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_tag_names_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.tag_names is None


@pytest.mark.contract_test
def test_accepts_single_tag_name() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names="gnp",
    )
    assert p.tag_names == "gnp"


@pytest.mark.contract_test
def test_accepts_semicolon_separated_tag_names() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_names="gnp;quarterly",
    )
    assert p.tag_names == "gnp;quarterly"


@pytest.mark.contract_test
def test_rejects_invalid_tag_names() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            tag_names="gnp;",
        )


@pytest.mark.contract_test
def test_tag_group_id_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.tag_group_id is None


@pytest.mark.contract_test
def test_accepts_explicit_tag_group_id() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        tag_group_id=TagGroupID.freq,
    )
    assert p.tag_group_id == TagGroupID.freq


@pytest.mark.contract_test
def test_search_text_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.search_text is None


@pytest.mark.contract_test
def test_accepts_explicit_search_text() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        search_text="commercial paper",
    )
    assert p.search_text == "commercial paper"


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        order_by=OrderBy.series_count,
    )
    assert p.order_by == OrderBy.series_count


@pytest.mark.contract_test
def test_accepts_explicit_sort_order() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        sort_order=SortOrder.desc,
    )
    assert p.sort_order == SortOrder.desc


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_release_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            limit=1001,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            offset=-1,
        )
