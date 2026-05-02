import pytest

from fred import for_request, source_releases
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SOURCE_ID = 1


@pytest.mark.integration_test
def test_source_releases_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = source_releases.RequestParams(
        api_key=api_key,
        file_type=source_releases.FileType.json,
        source_id=_SOURCE_ID,
    )
    data = fred_get_json(str(source_releases.ENDPOINT), for_request(params))
    response = source_releases.Response.model_validate(data)
    assert len(response.releases) >= 1


@pytest.mark.integration_test
def test_source_releases_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = source_releases.RequestParams(
        api_key=api_key,
        file_type=source_releases.FileType.xml,
        source_id=_SOURCE_ID,
    )
    root = fred_get_xml(str(source_releases.ENDPOINT), for_request(params))
    assert root.tag == "releases"
