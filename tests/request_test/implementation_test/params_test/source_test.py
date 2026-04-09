from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import ValidationError
import pytest

from fred.request.implementation.file_type import FileType
from fred.request.implementation.params.source import Params

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_SOURCE_ID = 1
_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


# api_key


@pytest.mark.unit_test
def test_api_key_required() -> None:
    with pytest.raises(ValidationError):
        Params(source_id=VALID_SOURCE_ID, file_type=FileType.json)  # type: ignore[call-arg]


# source_id


@pytest.mark.unit_test
def test_source_id_required() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.unit_test
def test_source_id_accepts_positive_int() -> None:
    assert (
        Params(api_key=VALID_KEY, source_id=1, file_type=FileType.json).source_id == 1
    )


@pytest.mark.unit_test
def test_source_id_raises_on_zero() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, source_id=0, file_type=FileType.json)


@pytest.mark.unit_test
def test_source_id_raises_on_negative() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, source_id=-1, file_type=FileType.json)


# file_type


@pytest.mark.unit_test
def test_file_type_required() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)  # type: ignore[call-arg]


@pytest.mark.unit_test
def test_file_type_accepts_json() -> None:
    assert (
        Params(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.json
        ).file_type
        == FileType.json
    )


@pytest.mark.unit_test
def test_file_type_accepts_xml() -> None:
    assert (
        Params(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.xml
        ).file_type
        == FileType.xml
    )


@pytest.mark.unit_test
def test_file_type_raises_on_invalid() -> None:
    with pytest.raises(ValidationError):
        Params(api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type="csv")  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


# realtime_start


@pytest.mark.unit_test
def test_realtime_start_defaults_to_today_in_st_louis() -> None:
    assert (
        Params(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.json
        ).realtime_start
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_start_accepts_valid_date() -> None:
    assert (
        Params(
            api_key=VALID_KEY,
            source_id=VALID_SOURCE_ID,
            file_type=FileType.json,
            realtime_start="2024-01-15",
        ).realtime_start
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_start_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Params(
            api_key=VALID_KEY,
            source_id=VALID_SOURCE_ID,
            file_type=FileType.json,
            realtime_start="not-a-date",
        )


# realtime_end


@pytest.mark.unit_test
def test_realtime_end_defaults_to_today_in_st_louis() -> None:
    assert (
        Params(
            api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.json
        ).realtime_end
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


@pytest.mark.unit_test
def test_realtime_end_accepts_valid_date() -> None:
    assert (
        Params(
            api_key=VALID_KEY,
            source_id=VALID_SOURCE_ID,
            file_type=FileType.json,
            realtime_end="2024-01-15",
        ).realtime_end
        == "2024-01-15"
    )


@pytest.mark.unit_test
def test_realtime_end_raises_on_invalid_date() -> None:
    with pytest.raises(ValidationError):
        Params(
            api_key=VALID_KEY,
            source_id=VALID_SOURCE_ID,
            file_type=FileType.json,
            realtime_end="not-a-date",
        )


# for_request


@pytest.mark.unit_test
def test_for_request_returns_all_fields_as_strings() -> None:
    result = Params(
        api_key=VALID_KEY,
        source_id=VALID_SOURCE_ID,
        file_type=FileType.json,
        realtime_start="2024-01-15",
        realtime_end="2024-01-15",
    ).for_request()
    assert result == {
        "api_key": VALID_KEY,
        "source_id": str(VALID_SOURCE_ID),
        "file_type": "json",
        "realtime_start": "2024-01-15",
        "realtime_end": "2024-01-15",
    }


@pytest.mark.unit_test
def test_for_request_excludes_none_values() -> None:
    result = Params(
        api_key=VALID_KEY, source_id=VALID_SOURCE_ID, file_type=FileType.json
    ).for_request()
    assert "None" not in result.values()
