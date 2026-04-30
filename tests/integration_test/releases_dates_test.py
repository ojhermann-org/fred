import pytest

from fred import for_request, releases_dates
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_releases_dates_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = releases_dates.RequestParams(
        api_key=api_key,
        file_type=releases_dates.FileType.json,
    )
    data = fred_get_json(str(releases_dates.ENDPOINT), for_request(params))
    response = releases_dates.Response.model_validate(data)
    assert len(response.release_dates) >= 1


@pytest.mark.integration_test
def test_releases_dates_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = releases_dates.RequestParams(
        api_key=api_key,
        file_type=releases_dates.FileType.xml,
    )
    root = fred_get_xml(str(releases_dates.ENDPOINT), for_request(params))
    assert root.tag == "release_dates"
    assert len(root.findall("release_date")) >= 1
