import pytest

from fred import for_request, series_search
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_series_search_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_search.RequestParams(
        api_key=api_key,
        file_type=series_search.FileType.json,
        search_text="monetary service index",
    )
    data = fred_get_json(str(series_search.ENDPOINT), for_request(params))
    response = series_search.Response.model_validate(data)
    assert len(response.seriess) >= 1


@pytest.mark.integration_test
def test_series_search_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_search.RequestParams(
        api_key=api_key,
        file_type=series_search.FileType.xml,
        search_text="monetary service index",
    )
    root = fred_get_xml(str(series_search.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
