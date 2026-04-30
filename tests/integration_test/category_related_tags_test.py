import pytest

from fred import category_related_tags, for_request
from tests.integration_test.conftest import FredGetJson, FredGetXml

_CATEGORY_ID = 125  # Trade & International Transactions — used in API docs example
_TAG_NAMES = "services;quarterly"


@pytest.mark.integration_test
def test_category_related_tags_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = category_related_tags.RequestParams(
        api_key=api_key,
        file_type=category_related_tags.FileType.json,
        category_id=_CATEGORY_ID,
        tag_names=_TAG_NAMES,
    )
    data = fred_get_json(str(category_related_tags.ENDPOINT), for_request(params))
    response = category_related_tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_category_related_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = category_related_tags.RequestParams(
        api_key=api_key,
        file_type=category_related_tags.FileType.xml,
        category_id=_CATEGORY_ID,
        tag_names=_TAG_NAMES,
    )
    root = fred_get_xml(str(category_related_tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
    assert len(root.findall("tag")) >= 1
