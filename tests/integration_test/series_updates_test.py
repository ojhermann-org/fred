import pytest

from fred import for_request, series_updates
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_series_updates_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_updates.RequestParams(
        api_key=api_key,
        file_type=series_updates.FileType.json,
    )
    data = fred_get_json(str(series_updates.ENDPOINT), for_request(params))
    response = series_updates.Response.model_validate(data)
    assert isinstance(response.seriess, list)


@pytest.mark.integration_test
def test_series_updates_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_updates.RequestParams(
        api_key=api_key,
        file_type=series_updates.FileType.xml,
    )
    root = fred_get_xml(str(series_updates.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
