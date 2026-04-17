import pytest

from fred import category_children, for_request
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_category_children_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = category_children.RequestParams(
        api_key=api_key,
        file_type=category_children.FileType.json,
        category_id=0,
    )
    data = fred_get_json(str(category_children.ENDPOINT), for_request(params))
    response = category_children.Response.model_validate(data)
    assert len(response.categories) >= 1
    assert all(c.parent_id == 0 for c in response.categories)


@pytest.mark.integration_test
def test_category_children_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = category_children.RequestParams(
        api_key=api_key,
        file_type=category_children.FileType.xml,
        category_id=0,
    )
    root = fred_get_xml(str(category_children.ENDPOINT), for_request(params))
    assert root.tag == "categories"
    categories = root.findall("category")
    assert len(categories) >= 1
    assert all(c.get("parent_id") == "0" for c in categories)
