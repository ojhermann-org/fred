import pytest

from fred import for_request, release_series
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 51


@pytest.mark.integration_test
def test_release_series_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release_series.RequestParams(
        api_key=api_key,
        file_type=release_series.FileType.json,
        release_id=_RELEASE_ID,
    )
    data = fred_get_json(str(release_series.ENDPOINT), for_request(params))
    response = release_series.Response.model_validate(data)
    assert len(response.series) >= 1


@pytest.mark.integration_test
def test_release_series_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release_series.RequestParams(
        api_key=api_key,
        file_type=release_series.FileType.xml,
        release_id=_RELEASE_ID,
    )
    root = fred_get_xml(str(release_series.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
    assert len(root.findall("series")) >= 1
