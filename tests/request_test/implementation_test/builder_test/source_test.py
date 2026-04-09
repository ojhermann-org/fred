from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from request.enum.endpoint import Endpoint
from request.implementation.builder.source import Builder
from request.implementation.file_type import FileType

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_SOURCE_ID = 1
_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


# build — endpoint


@pytest.mark.unit_test
def test_build_returns_source_endpoint() -> None:
    assert (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID).build().endpoint()
        == Endpoint.source
    )


# build — default parameters


@pytest.mark.unit_test
def test_build_default_file_type_is_json() -> None:
    assert (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .build()
        .parameters()["file_type"]
        == "json"
    )


@pytest.mark.unit_test
def test_build_default_realtime_start_is_today_in_st_louis() -> None:
    assert (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .build()
        .parameters()["realtime_start"]
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


@pytest.mark.unit_test
def test_build_default_realtime_end_is_today_in_st_louis() -> None:
    assert (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .build()
        .parameters()["realtime_end"]
        == datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
    )


# file_type


@pytest.mark.unit_test
def test_file_type_sets_file_type() -> None:
    result = (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .file_type(FileType.xml)
        .build()
    )
    assert result.parameters()["file_type"] == "xml"


@pytest.mark.unit_test
def test_file_type_returns_builder_for_chaining() -> None:
    builder = Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
    assert builder.file_type(FileType.xml) is builder


# realtime_start


@pytest.mark.unit_test
def test_realtime_start_sets_realtime_start() -> None:
    result = (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .realtime_start("2024-01-15")
        .build()
    )
    assert result.parameters()["realtime_start"] == "2024-01-15"


@pytest.mark.unit_test
def test_realtime_start_returns_builder_for_chaining() -> None:
    builder = Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
    assert builder.realtime_start("2024-01-15") is builder


# realtime_end


@pytest.mark.unit_test
def test_realtime_end_sets_realtime_end() -> None:
    result = (
        Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
        .realtime_end("2024-01-15")
        .build()
    )
    assert result.parameters()["realtime_end"] == "2024-01-15"


@pytest.mark.unit_test
def test_realtime_end_returns_builder_for_chaining() -> None:
    builder = Builder(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
    assert builder.realtime_end("2024-01-15") is builder
