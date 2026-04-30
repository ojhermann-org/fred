import pytest

from fred import for_request, release_sources
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 51


@pytest.mark.integration_test
def test_release_sources_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release_sources.RequestParams(
        api_key=api_key,
        file_type=release_sources.FileType.json,
        release_id=_RELEASE_ID,
    )
    data = fred_get_json(str(release_sources.ENDPOINT), for_request(params))
    response = release_sources.Response.model_validate(data)
    assert len(response.sources) >= 1


@pytest.mark.integration_test
def test_release_sources_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release_sources.RequestParams(
        api_key=api_key,
        file_type=release_sources.FileType.xml,
        release_id=_RELEASE_ID,
    )
    root = fred_get_xml(str(release_sources.ENDPOINT), for_request(params))
    assert root.tag == "sources"
    assert len(root.findall("source")) >= 1
