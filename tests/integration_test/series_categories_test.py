import pytest

from fred import for_request, series_categories
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "EXJPUS"


@pytest.mark.integration_test
def test_series_categories_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_categories.RequestParams(
        api_key=api_key,
        file_type=series_categories.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series_categories.ENDPOINT), for_request(params))
    response = series_categories.Response.model_validate(data)
    assert len(response.categories) >= 1


@pytest.mark.integration_test
def test_series_categories_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_categories.RequestParams(
        api_key=api_key,
        file_type=series_categories.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series_categories.ENDPOINT), for_request(params))
    assert root.tag == "categories"
