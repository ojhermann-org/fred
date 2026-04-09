import json
import urllib.parse
import urllib.request

import pytest

from fred.request import FileType, RequestBuilder


@pytest.mark.integration_test
def test_source_request_returns_valid_response(api_key: str) -> None:
    request = RequestBuilder.source()(
        api_key=api_key,
        source_id=1,
        file_type=FileType.json,
    ).build()
    url = str(request.endpoint()) + "?" + urllib.parse.urlencode(request.parameters())
    with urllib.request.urlopen(url) as resp:
        body = json.loads(resp.read().decode())
    assert "sources" in body
    assert len(body["sources"]) > 0
    assert body["sources"][0]["id"] == 1
