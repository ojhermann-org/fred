import pytest

from fred import for_request, series_vintagedates
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "GNPCA"


@pytest.mark.integration_test
def test_series_vintagedates_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_vintagedates.RequestParams(
        api_key=api_key,
        file_type=series_vintagedates.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series_vintagedates.ENDPOINT), for_request(params))
    response = series_vintagedates.Response.model_validate(data)
    assert len(response.vintage_dates) >= 1


@pytest.mark.integration_test
def test_series_vintagedates_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_vintagedates.RequestParams(
        api_key=api_key,
        file_type=series_vintagedates.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series_vintagedates.ENDPOINT), for_request(params))
    assert root.tag == "vintage_dates"
