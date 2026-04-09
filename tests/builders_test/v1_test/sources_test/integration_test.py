import json
import urllib.parse
import urllib.request

import pytest

from builders.v1.sources.builder import Builder
from fred.v1.file_type import FileType
from fred.v1.sources.response import Response


@pytest.mark.integration_test
def test_get_sources_returns_valid_response(api_key: str) -> None:
    request = (
        Builder(api_key=api_key)
        .with_file_type(FileType.json)
        .with_realtime_start("2020-01-01")
        .with_realtime_end("2020-01-01")
        .build()
    )
    url = request.url + "?" + urllib.parse.urlencode(request.params)
    with urllib.request.urlopen(url) as resp:
        body = json.loads(resp.read().decode())
    response = Response.model_validate(body)
    assert len(response.sources) > 0
