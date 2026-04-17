import pytest

from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.category_request_params import CategoryRequestParams
from fred.types.category_response import Response
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_category_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = CategoryRequestParams(
        api_key=api_key,
        file_type=FileType.json,
        category_id=0,
    )
    data = fred_get_json(str(Endpoint.category), params.for_request())
    response = Response.model_validate(data)
    assert len(response.categories) == 1
    assert response.categories[0].id == 0
    assert response.categories[0].name == "Categories"
    assert response.categories[0].parent_id == 0


@pytest.mark.integration_test
def test_category_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = CategoryRequestParams(
        api_key=api_key,
        file_type=FileType.xml,
        category_id=0,
    )
    root = fred_get_xml(str(Endpoint.category), params.for_request())
    assert root.tag == "categories"
    categories = root.findall("category")
    assert len(categories) == 1
    assert categories[0].get("id") == "0"
    assert categories[0].get("name") == "Categories"
    assert categories[0].get("parent_id") == "0"
