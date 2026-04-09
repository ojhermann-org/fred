import pytest

from fred.request.enum.endpoint import Endpoint
from fred.request.implementation.request import Request

PARAMS: dict[str, str] = {"api_key": "abc123", "file_type": "json"}


@pytest.mark.unit_test
def test_endpoint_returns_given_endpoint() -> None:
    assert (
        Request(endpoint=Endpoint.source, parameters=PARAMS).endpoint()
        == Endpoint.source
    )


@pytest.mark.unit_test
def test_parameters_returns_given_parameters() -> None:
    assert Request(endpoint=Endpoint.source, parameters=PARAMS).parameters() == PARAMS


@pytest.mark.unit_test
def test_different_endpoints_are_returned_correctly() -> None:
    assert (
        Request(endpoint=Endpoint.sources, parameters=PARAMS).endpoint()
        == Endpoint.sources
    )
    assert (
        Request(endpoint=Endpoint.source_releases, parameters=PARAMS).endpoint()
        == Endpoint.source_releases
    )


@pytest.mark.unit_test
def test_empty_parameters_are_returned_correctly() -> None:
    assert Request(endpoint=Endpoint.source, parameters={}).parameters() == {}
