import pytest

from fred import for_request, release_dates
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 82


@pytest.mark.integration_test
def test_release_dates_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release_dates.RequestParams(
        api_key=api_key,
        file_type=release_dates.FileType.json,
        release_id=_RELEASE_ID,
    )
    data = fred_get_json(str(release_dates.ENDPOINT), for_request(params))
    response = release_dates.Response.model_validate(data)
    assert len(response.release_dates) >= 1
    assert all(rd.release_id == _RELEASE_ID for rd in response.release_dates)


@pytest.mark.integration_test
def test_release_dates_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release_dates.RequestParams(
        api_key=api_key,
        file_type=release_dates.FileType.xml,
        release_id=_RELEASE_ID,
    )
    root = fred_get_xml(str(release_dates.ENDPOINT), for_request(params))
    assert root.tag == "release_dates"
    assert len(root.findall("release_date")) >= 1
