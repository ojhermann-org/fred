import pytest

from fred import for_request, series
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "GNPCA"


@pytest.mark.integration_test
def test_series_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series.RequestParams(
        api_key=api_key,
        file_type=series.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series.ENDPOINT), for_request(params))
    response = series.Response.model_validate(data)
    assert len(response.seriess) >= 1
    assert response.seriess[0].id == _SERIES_ID


@pytest.mark.integration_test
def test_series_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series.RequestParams(
        api_key=api_key,
        file_type=series.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
