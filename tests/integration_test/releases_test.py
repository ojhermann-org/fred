import pytest

from fred import for_request, releases
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_releases_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = releases.RequestParams(
        api_key=api_key,
        file_type=releases.FileType.json,
    )
    data = fred_get_json(str(releases.ENDPOINT), for_request(params))
    response = releases.Response.model_validate(data)
    assert len(response.releases) >= 1


@pytest.mark.integration_test
def test_releases_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = releases.RequestParams(
        api_key=api_key,
        file_type=releases.FileType.xml,
    )
    root = fred_get_xml(str(releases.ENDPOINT), for_request(params))
    assert root.tag == "releases"
    assert len(root.findall("release")) >= 1
