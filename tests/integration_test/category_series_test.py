import pytest

from fred import category_series, for_request
from tests.integration_test.conftest import FredGetJson, FredGetXml

_CATEGORY_ID = 106  # National Income & Product Accounts — reliably has series


@pytest.mark.integration_test
def test_category_series_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = category_series.RequestParams(
        api_key=api_key,
        file_type=category_series.FileType.json,
        category_id=_CATEGORY_ID,
    )
    data = fred_get_json(str(category_series.ENDPOINT), for_request(params))
    response = category_series.Response.model_validate(data)
    assert len(response.series) >= 1


@pytest.mark.integration_test
def test_category_series_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = category_series.RequestParams(
        api_key=api_key,
        file_type=category_series.FileType.xml,
        category_id=_CATEGORY_ID,
    )
    root = fred_get_xml(str(category_series.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
    assert len(root.findall("series")) >= 1
