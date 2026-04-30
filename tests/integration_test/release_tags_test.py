import pytest

from fred import for_request, release_tags
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 86


@pytest.mark.integration_test
def test_release_tags_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release_tags.RequestParams(
        api_key=api_key,
        file_type=release_tags.FileType.json,
        release_id=_RELEASE_ID,
    )
    data = fred_get_json(str(release_tags.ENDPOINT), for_request(params))
    response = release_tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_release_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release_tags.RequestParams(
        api_key=api_key,
        file_type=release_tags.FileType.xml,
        release_id=_RELEASE_ID,
    )
    root = fred_get_xml(str(release_tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
    assert len(root.findall("tag")) >= 1
