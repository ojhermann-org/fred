from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.enums.order_by import SourceReleases as OrderBy
from fred.enums.sort_order import SortOrder
from fred.types.source_releases.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SOURCE_ID = 1


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        source_id=_VALID_SOURCE_ID,
    )
    assert p.source_id == _VALID_SOURCE_ID


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, source_id=_VALID_SOURCE_ID
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        source_id=_VALID_SOURCE_ID,
        order_by=OrderBy.name,
    )
    assert p.order_by == OrderBy.name


@pytest.mark.contract_test
def test_rejects_missing_source_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_source_id_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json, source_id=0)


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            source_id=_VALID_SOURCE_ID,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            source_id=_VALID_SOURCE_ID,
            limit=1001,
        )
