import pytest

from fred import for_request, series_search_related_tags
from tests.integration_test.conftest import FredGetJson, FredGetXml


@pytest.mark.integration_test
def test_series_search_related_tags_json(
    api_key: str, fred_get_json: FredGetJson
) -> None:
    params = series_search_related_tags.RequestParams(
        api_key=api_key,
        file_type=series_search_related_tags.FileType.json,
        series_search_text="monetary service index",
        tag_names="m2",
    )
    data = fred_get_json(str(series_search_related_tags.ENDPOINT), for_request(params))
    response = series_search_related_tags.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_series_search_related_tags_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = series_search_related_tags.RequestParams(
        api_key=api_key,
        file_type=series_search_related_tags.FileType.xml,
        series_search_text="monetary service index",
        tag_names="m2",
    )
    root = fred_get_xml(str(series_search_related_tags.ENDPOINT), for_request(params))
    assert root.tag == "tags"
