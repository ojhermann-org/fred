import pytest

from fred import for_request, release_tables
from tests.integration_test.conftest import FredGetJson, FredGetXml

_RELEASE_ID = 53
_ELEMENT_ID = 12886


@pytest.mark.integration_test
def test_release_tables_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = release_tables.RequestParams(
        api_key=api_key,
        file_type=release_tables.FileType.json,
        release_id=_RELEASE_ID,
        element_id=_ELEMENT_ID,
    )
    data = fred_get_json(str(release_tables.ENDPOINT), for_request(params))
    response = release_tables.Response.model_validate(data)
    assert response.element_id == _ELEMENT_ID
    assert len(response.elements) >= 1


@pytest.mark.integration_test
def test_release_tables_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = release_tables.RequestParams(
        api_key=api_key,
        file_type=release_tables.FileType.xml,
        release_id=_RELEASE_ID,
        element_id=_ELEMENT_ID,
    )
    root = fred_get_xml(str(release_tables.ENDPOINT), for_request(params))
    assert root.tag == "elements"
