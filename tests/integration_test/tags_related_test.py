import pytest

from fred import for_request, tags_related
from tests.integration_test.conftest import FredGetJson, FredGetXml

_TAG_NAMES = "monetary aggregates;weekly"


@pytest.mark.integration_test
def test_tags_related_json(api_key: str, fred_get_json: FredGetJson) -> None:
    params = tags_related.RequestParams(
        api_key=api_key,
        file_type=tags_related.FileType.json,
        tag_names=_TAG_NAMES,
    )
    data = fred_get_json(str(tags_related.ENDPOINT), for_request(params))
    response = tags_related.Response.model_validate(data)
    assert len(response.tags) >= 1


@pytest.mark.integration_test
def test_tags_related_xml(api_key: str, fred_get_xml: FredGetXml) -> None:
    params = tags_related.RequestParams(
        api_key=api_key,
        file_type=tags_related.FileType.xml,
        tag_names=_TAG_NAMES,
    )
    root = fred_get_xml(str(tags_related.ENDPOINT), for_request(params))
    assert root.tag == "tags"
