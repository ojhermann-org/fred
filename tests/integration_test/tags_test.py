import pytest

from fred import for_request, tags
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_tags_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = tags.RequestParams(
        api_key=api_key,
        file_type=tags.FileType.json,
    )
    data = fred_get_json(str(tags.ENDPOINT), for_request(params))
    response = tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = tags.RequestParams(
        api_key=api_key,
        file_type=tags.FileType.xml,
    )
    root = fred_get_xml(str(tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
