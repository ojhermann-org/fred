from datetime import date

from pydantic import ValidationError
import pytest

from fred.v1.file_type import FileType
from fred.v1.sort_order import SortOrder
from fred.v1.source_releases.order_by import OrderBy
from fred.v1.source_releases.parameters import Parameters

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_SOURCE_ID = 1


# api_key


@pytest.mark.unit_test
def test_api_key_required() -> None:
    with pytest.raises(ValidationError):
        Parameters(source_id=VALID_SOURCE_ID)  # type: ignore[call-arg]


# source_id


@pytest.mark.unit_test
def test_source_id_required() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY)  # type: ignore[call-arg]


@pytest.mark.unit_test
def test_source_id_accepts_positive_int() -> None:
    assert Parameters(api_key=VALID_KEY, source_id=1).source_id == 1


@pytest.mark.unit_test
def test_source_id_raises_on_zero() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=0)


@pytest.mark.unit_test
def test_source_id_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=-1)


# file_type


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_file_type_defaults_to_xml() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).file_type
        == FileType.xml
    )


@pytest.mark.unit_test
def test_file_type_accepts_xml() -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.xml
        ).file_type
        == FileType.xml
    )


@pytest.mark.unit_test
def test_file_type_accepts_json() -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.json
        ).file_type
        == FileType.json
    )


@pytest.mark.unit_test
def test_file_type_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type="csv")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# realtime_start


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_realtime_start_defaults_to_today() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).realtime_start
        == date.today().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_start_accepts_valid_date() -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, realtime_start="2024-01-15"
        ).realtime_start
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_start_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, realtime_start="not-a-date"
        )


# realtime_end


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_realtime_end_defaults_to_today() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).realtime_end
        == date.today().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_end_accepts_valid_date() -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, realtime_end="2024-01-15"
        ).realtime_end
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_end_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, realtime_end="not-a-date"
        )


# limit


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_limit_defaults_to_1000() -> None:
    assert Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).limit == 1000


@pytest.mark.unit_test
def test_limit_accepts_1() -> None:
    assert Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, limit=1).limit == 1


@pytest.mark.unit_test
def test_limit_accepts_1000() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, limit=1000).limit
        == 1000
    )


@pytest.mark.unit_test
def test_limit_raises_on_zero() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, limit=0)


@pytest.mark.unit_test
def test_limit_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, limit=-1)


@pytest.mark.unit_test
def test_limit_raises_on_greater_than_1000() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, limit=1001)


# offset


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_offset_defaults_to_0() -> None:
    assert Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).offset == 0


@pytest.mark.unit_test
def test_offset_accepts_0() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, offset=0).offset == 0
    )


@pytest.mark.unit_test
def test_offset_accepts_positive() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, offset=10).offset == 10
    )


@pytest.mark.unit_test
def test_offset_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, offset=-1)


# order_by


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_order_by_defaults_to_release_id() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).order_by
        == OrderBy.release_id
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
@pytest.mark.parametrize("value", list(OrderBy))
def test_order_by_accepts_all_values(value: OrderBy) -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, order_by=value
        ).order_by
        == value
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_order_by_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, order_by="invalid")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# sort_order


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_sort_order_defaults_to_asc() -> None:
    assert (
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).sort_order
        == SortOrder.asc
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
@pytest.mark.parametrize("value", list(SortOrder))
def test_sort_order_accepts_all_values(value: SortOrder) -> None:
    assert (
        Parameters(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, sort_order=value
        ).sort_order
        == value
    )


@pytest.mark.contract_test
@pytest.mark.unit_test
def test_sort_order_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Parameters(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, sort_order="invalid")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]
