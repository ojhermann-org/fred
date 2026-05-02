import pytest

from fred import for_request, sources
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_sources_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = sources.RequestParams(
        api_key=api_key,
        file_type=sources.FileType.json,
    )
    data = fred_get_json(str(sources.ENDPOINT), for_request(params))
    response = sources.Response.model_validate(data)
    assert len(response.sources) >= 1


@pytest.mark.integration_test
def test_sources_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = sources.RequestParams(
        api_key=api_key,
        file_type=sources.FileType.xml,
    )
    root = fred_get_xml(str(sources.ENDPOINT), for_request(params))
    assert root.tag == "sources"
