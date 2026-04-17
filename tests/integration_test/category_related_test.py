import pytest

from fred import category_related, for_request
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_category_related_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = category_related.RequestParams(
        api_key=api_key,
        file_type=category_related.FileType.json,
        category_id=32073,
    )
    data = fred_get_json(str(category_related.ENDPOINT), for_request(params))
    response = category_related.Response.model_validate(data)
    assert len(response.categories) >= 1


@pytest.mark.integration_test
def test_category_related_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = category_related.RequestParams(
        api_key=api_key,
        file_type=category_related.FileType.xml,
        category_id=32073,
    )
    root = fred_get_xml(str(category_related.ENDPOINT), for_request(params))
    assert root.tag == "categories"
    assert len(root.findall("category")) >= 1
