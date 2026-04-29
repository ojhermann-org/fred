import pytest

from fred import category_tags, for_request
from tests.integration_test.conftest import FredGetJson, FredGetXml

_CATEGORY_ID = 106  # National Income & Product Accounts — reliably has tags


@pytest.mark.integration_test
def test_category_tags_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = category_tags.RequestParams(
        api_key=api_key,
        file_type=category_tags.FileType.json,
        category_id=_CATEGORY_ID,
    )
    data = fred_get_json(str(category_tags.ENDPOINT), for_request(params))
    response = category_tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_category_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = category_tags.RequestParams(
        api_key=api_key,
        file_type=category_tags.FileType.xml,
        category_id=_CATEGORY_ID,
    )
    root = fred_get_xml(str(category_tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
    assert len(root.findall("tag")) >= 1
