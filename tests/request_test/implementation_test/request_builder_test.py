import pytest

from fred.request.enum.endpoint import Endpoint
from fred.request.implementation.request_builder import RequestBuilder

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
VALID_SOURCE_ID = 1


@pytest.mark.unit_test
def test_source_returns_a_builder_type() -> None:
    builder_class = RequestBuilder.source()
    instance = builder_class(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)
    assert callable(getattr(instance, "build", None))


@pytest.mark.unit_test
def test_source_returned_class_is_instantiable() -> None:
    RequestBuilder.source()(api_key=VALID_KEY, source_id=VALID_SOURCE_ID)


@pytest.mark.unit_test
def test_source_returned_class_builds_request_with_correct_endpoint() -> None:
    request = RequestBuilder.source()(
        api_key=VALID_KEY, source_id=VALID_SOURCE_ID
    ).build()
    assert request.endpoint() == Endpoint.source
