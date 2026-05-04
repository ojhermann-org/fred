import pytest

from fred import for_request, geofred_series_data
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "WIPCPI"
_DATE = "2012-01-01"
_START_DATE = "2010-01-01"


@pytest.mark.integration_test
def test_geofred_series_data_json_single_date(
    api_key: str, fred_get_json: FredGetJson
) -> None:
    params = geofred_series_data.RequestParams(
        api_key=api_key,
        file_type=geofred_series_data.FileType.json,
        series_id=_SERIES_ID,
        date=_DATE,
    )
    data = fred_get_json(str(geofred_series_data.ENDPOINT), for_request(params))
    response = geofred_series_data.Response.model_validate(data)
    assert response.meta.region == "state"
    assert response.meta.data is not None
    assert _DATE in response.meta.data
    obs = response.meta.data[_DATE]
    assert len(obs) >= 1
    assert any(o.series_id == "ALPCPI" for o in obs)


@pytest.mark.integration_test
def test_geofred_series_data_json_range(
    api_key: str, fred_get_json: FredGetJson
) -> None:
    params = geofred_series_data.RequestParams(
        api_key=api_key,
        file_type=geofred_series_data.FileType.json,
        series_id=_SERIES_ID,
        start_date=_START_DATE,
        date=_DATE,
    )
    data = fred_get_json(str(geofred_series_data.ENDPOINT), for_request(params))
    response = geofred_series_data.Response.model_validate(data)
    assert response.meta.data is not None
    assert len(response.meta.data) >= 2


@pytest.mark.integration_test
def test_geofred_series_data_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = geofred_series_data.RequestParams(
        api_key=api_key,
        file_type=geofred_series_data.FileType.xml,
        series_id=_SERIES_ID,
        date=_DATE,
    )
    root = fred_get_xml(str(geofred_series_data.ENDPOINT), for_request(params))
    assert root.tag == "series_data"
