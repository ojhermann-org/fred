import pytest

from fred import for_request, series_observations
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "GNPCA"


@pytest.mark.integration_test
def test_series_observations_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_observations.RequestParams(
        api_key=api_key,
        file_type=series_observations.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series_observations.ENDPOINT), for_request(params))
    response = series_observations.Response.model_validate(data)
    assert len(response.observations) >= 1


@pytest.mark.integration_test
def test_series_observations_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_observations.RequestParams(
        api_key=api_key,
        file_type=series_observations.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series_observations.ENDPOINT), for_request(params))
    assert root.tag == "observations"
