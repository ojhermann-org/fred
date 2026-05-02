import pytest

from fred import for_request, tags_series
from tests.integration_test.conftest import FredGetJson, FredGetXml

_TAG_NAMES = "slovenia;food;oecd"


@pytest.mark.integration_test
def test_tags_series_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = tags_series.RequestParams(
        api_key=api_key,
        file_type=tags_series.FileType.json,
        tag_names=_TAG_NAMES,
    )
    data = fred_get_json(str(tags_series.ENDPOINT), for_request(params))
    response = tags_series.Response.model_validate(data)
    assert len(response.seriess) >= 1


@pytest.mark.integration_test
def test_tags_series_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = tags_series.RequestParams(
        api_key=api_key,
        file_type=tags_series.FileType.xml,
        tag_names=_TAG_NAMES,
    )
    root = fred_get_xml(str(tags_series.ENDPOINT), for_request(params))
    assert root.tag == "seriess"
