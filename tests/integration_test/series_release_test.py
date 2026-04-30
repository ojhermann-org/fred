import pytest

from fred import for_request, series_release
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "IRA"


@pytest.mark.integration_test
def test_series_release_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_release.RequestParams(
        api_key=api_key,
        file_type=series_release.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series_release.ENDPOINT), for_request(params))
    response = series_release.Response.model_validate(data)
    assert len(response.releases) >= 1


@pytest.mark.integration_test
def test_series_release_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_release.RequestParams(
        api_key=api_key,
        file_type=series_release.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series_release.ENDPOINT), for_request(params))
    assert root.tag == "releases"
