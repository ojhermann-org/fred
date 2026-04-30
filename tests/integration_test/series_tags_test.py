import pytest

from fred import for_request, series_tags
from tests.integration_test.conftest import FredGetJson, FredGetXml

_SERIES_ID = "GNPCA"


@pytest.mark.integration_test
def test_series_tags_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = series_tags.RequestParams(
        api_key=api_key,
        file_type=series_tags.FileType.json,
        series_id=_SERIES_ID,
    )
    data = fred_get_json(str(series_tags.ENDPOINT), for_request(params))
    response = series_tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_series_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_tags.RequestParams(
        api_key=api_key,
        file_type=series_tags.FileType.xml,
        series_id=_SERIES_ID,
    )
    root = fred_get_xml(str(series_tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
