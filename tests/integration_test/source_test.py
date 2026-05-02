import pytest

from fred import for_request, source
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SOURCE_ID = 1


@pytest.mark.integration_test
def test_source_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = source.RequestParams(
        api_key=api_key,
        file_type=source.FileType.json,
        source_id=_SOURCE_ID,
    )
    data = fred_get_json(str(source.ENDPOINT), for_request(params))
    response = source.Response.model_validate(data)
    assert len(response.sources) == 1
    assert response.sources[0].id == _SOURCE_ID


@pytest.mark.integration_test
def test_source_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = source.RequestParams(
        api_key=api_key,
        file_type=source.FileType.xml,
        source_id=_SOURCE_ID,
    )
    root = fred_get_xml(str(source.ENDPOINT), for_request(params))
    assert root.tag == "sources"
