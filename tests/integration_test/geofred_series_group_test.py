import pytest

from fred import for_request, geofred_series_group
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "SMU56000000500000001a"


@pytest.mark.integration_test
def test_geofred_series_group_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = geofred_series_group.RequestParams(
        api_key=api_key,
        file_type=geofred_series_group.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(geofred_series_group.ENDPOINT), for_request(params))
    response = geofred_series_group.Response.model_validate(data)
    assert response.series_group.title
    assert response.series_group.region_type == "state"
    assert response.series_group.frequency == "Annual"


@pytest.mark.integration_test
def test_geofred_series_group_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = geofred_series_group.RequestParams(
        api_key=api_key,
        file_type=geofred_series_group.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(geofred_series_group.ENDPOINT), for_request(params))
    assert root.tag == "series_meta"
