from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import ValidationError
import pytest

from request.implementation.file_type import FileType
from request.implementation.params.sources.main import Params
from request.implementation.params.sources.order_by import OrderBy
from request.implementation.sort_order import SortOrder

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


# api_key


@pytest.mark.unit_test
def test_api_key_required() -> None:
    with pytest.raises(ValidationError):
        Params(file_type=FileType.json)  # type: ignore[call-arg]


# file_type


@pytest.mark.unit_test
def test_file_type_required() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY)  # type: ignore[call-arg]


@pytest.mark.unit_test
def test_file_type_accepts_json() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json).file_type == FileType.json


@pytest.mark.unit_test
def test_file_type_accepts_xml() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.xml).file_type == FileType.xml


@pytest.mark.unit_test
def test_file_type_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type="csv")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# realtime_start


@pytest.mark.unit_test
def test_realtime_start_defaults_to_today_in_st_louis() -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json).realtime_start
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_start_accepts_valid_date() -> None:
    assert (
        Params(
            api_key=VALID_KEY, file_type=FileType.json, realtime_start="2024-01-15"
        ).realtime_start
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_start_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, realtime_start="not-a-date")


# realtime_end


@pytest.mark.unit_test
def test_realtime_end_defaults_to_today_in_st_louis() -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json).realtime_end
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_end_accepts_valid_date() -> None:
    assert (
        Params(
            api_key=VALID_KEY, file_type=FileType.json, realtime_end="2024-01-15"
        ).realtime_end
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_end_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, realtime_end="not-a-date")


# limit


@pytest.mark.unit_test
def test_limit_defaults_to_1000() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json).limit == 1000


@pytest.mark.unit_test
def test_limit_accepts_1() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json, limit=1).limit == 1


@pytest.mark.unit_test
def test_limit_accepts_1000() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json, limit=1000).limit == 1000


@pytest.mark.unit_test
def test_limit_raises_on_zero() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, limit=0)


@pytest.mark.unit_test
def test_limit_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, limit=-1)


@pytest.mark.unit_test
def test_limit_raises_on_greater_than_1000() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, limit=1001)


# offset


@pytest.mark.unit_test
def test_offset_defaults_to_0() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json).offset == 0


@pytest.mark.unit_test
def test_offset_accepts_0() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json, offset=0).offset == 0


@pytest.mark.unit_test
def test_offset_accepts_positive() -> None:
    assert Params(api_key=VALID_KEY, file_type=FileType.json, offset=10).offset == 10


@pytest.mark.unit_test
def test_offset_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, offset=-1)


# order_by


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_order_by_defaults_to_source_id() -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json).order_by == OrderBy.source_id
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
@pytest.mark.parametrize("value", list(OrderBy))
def test_order_by_accepts_all_values(value: OrderBy) -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json, order_by=value).order_by
        == value
    )


@pytest.mark.unit_test
def test_order_by_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, order_by="invalid")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# sort_order


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_sort_order_defaults_to_asc() -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json).sort_order == SortOrder.asc
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
@pytest.mark.parametrize("value", list(SortOrder))
def test_sort_order_accepts_all_values(value: SortOrder) -> None:
    assert (
        Params(api_key=VALID_KEY, file_type=FileType.json, sort_order=value).sort_order
        == value
    )


@pytest.mark.unit_test
def test_sort_order_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json, sort_order="invalid")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# for_request


@pytest.mark.unit_test
def test_for_request_returns_all_fields_as_strings() -> None:
    result = Params(
        api_key=VALID_KEY,
        file_type=FileType.json,
        realtime_start="2024-01-15",
        realtime_end="2024-01-15",
        limit=10,
        offset=5,
        order_by=OrderBy.name,
        sort_order=SortOrder.desc,
    ).for_request()
    assert result == {
        "api_key": VALID_KEY,
        "file_type": "json",
        "realtime_start": "2024-01-15",
        "realtime_end": "2024-01-15",
        "limit": "10",
        "offset": "5",
        "order_by": "name",
        "sort_order": "desc",
    }


@pytest.mark.unit_test
def test_for_request_excludes_none_values() -> None:
    result = Params(api_key=VALID_KEY, file_type=FileType.json).for_request()
    assert "None" not in result.values()
