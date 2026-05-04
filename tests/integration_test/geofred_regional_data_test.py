import pytest

from fred import for_request, geofred_regional_data
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_GROUP = "882"
_DATE = "2013-01-01"
_START_DATE = "2010-01-01"


@pytest.mark.integration_test
def test_geofred_regional_data_json_required_only(
    api_key: str, fred_get_json: FredGetJson
) -> None:
    params = geofred_regional_data.RequestParams(
        api_key=api_key,
        file_type=geofred_regional_data.FileType.json,
        series_group=_SERIES_GROUP,
        region_type=geofred_regional_data.Shape.state,
        date=_DATE,
        season=geofred_regional_data.SeasonalAdjustmentShort.nsa,
        units="Dollars",
        frequency=geofred_regional_data.Frequency.annual,
    )
    data = fred_get_json(str(geofred_regional_data.ENDPOINT), for_request(params))
    response = geofred_regional_data.Response.model_validate(data)
    assert response.meta.region == "state"
    assert response.meta.data is not None
    assert _DATE in response.meta.data
    obs = response.meta.data[_DATE]
    assert any(o.series_id == "ALPCPI" for o in obs)


@pytest.mark.integration_test
def test_geofred_regional_data_json_with_optional_params(
    api_key: str, fred_get_json: FredGetJson
) -> None:
    params = geofred_regional_data.RequestParams(
        api_key=api_key,
        file_type=geofred_regional_data.FileType.json,
        series_group=_SERIES_GROUP,
        region_type=geofred_regional_data.Shape.state,
        date=_DATE,
        season=geofred_regional_data.SeasonalAdjustmentShort.nsa,
        units="Dollars",
        frequency=geofred_regional_data.Frequency.annual,
        start_date=_START_DATE,
        transformation=geofred_regional_data.Units.levels,
        aggregation_method=geofred_regional_data.AggregationMethod.average,
    )
    data = fred_get_json(str(geofred_regional_data.ENDPOINT), for_request(params))
    response = geofred_regional_data.Response.model_validate(data)
    assert response.meta.data is not None
    assert len(response.meta.data) >= 2


@pytest.mark.integration_test
def test_geofred_regional_data_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = geofred_regional_data.RequestParams(
        api_key=api_key,
        file_type=geofred_regional_data.FileType.xml,
        series_group=_SERIES_GROUP,
        region_type=geofred_regional_data.Shape.state,
        date=_DATE,
        season=geofred_regional_data.SeasonalAdjustmentShort.nsa,
        units="Dollars",
        frequency=geofred_regional_data.Frequency.annual,
    )
    root = fred_get_xml(str(geofred_regional_data.ENDPOINT), for_request(params))
    assert root.tag == "series_data"
