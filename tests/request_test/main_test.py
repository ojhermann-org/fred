import pytest

from request.enum.endpoint import Endpoint
from request.implementation.builder.source import Builder as SourceBuilder
from request.main import RequestBuilder

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_SOURCE_ID = 1


@pytest.mark.unit_test
def test_source_returns_source_builder_class() -> None:
    assert RequestBuilder.source() is SourceBuilder


@pytest.mark.unit_test
def test_source_returned_class_is_instantiable() -> None:
    builder = RequestBuilder.source()(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
    assert isinstance(builder, SourceBuilder)


@pytest.mark.unit_test
def test_source_returned_class_builds_request_with_correct_endpoint() -> None:
    request = RequestBuilder.source()(
        api_key=VALID_KEY, source_id=VALID_SOURCE_ID
    ).build()
    assert request.endpoint() == Endpoint.source
