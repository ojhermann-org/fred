import pytest

from fred import for_request, release
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 53


@pytest.mark.integration_test
def test_release_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release.RequestParams(
        api_key=api_key,
        file_type=release.FileType.json,
        release_id=_RELEASE_ID,
    )
    data = fred_get_json(str(release.ENDPOINT), for_request(params))
    response = release.Response.model_validate(data)
    assert len(response.releases) == 1
    assert response.releases[0].id == _RELEASE_ID


@pytest.mark.integration_test
def test_release_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release.RequestParams(
        api_key=api_key,
        file_type=release.FileType.xml,
        release_id=_RELEASE_ID,
    )
    root = fred_get_xml(str(release.ENDPOINT), for_request(params))
    assert root.tag == "releases"
    releases = root.findall("release")
    assert len(releases) == 1
    assert releases[0].get("id") == str(_RELEASE_ID)
