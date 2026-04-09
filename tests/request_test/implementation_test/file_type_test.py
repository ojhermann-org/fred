import pytest

from fred.request.implementation.file_type import FileType


@pytest.mark.contract_test
def test_json_value() -> None:
    assert FileType.json == "json"


@pytest.mark.contract_test
def test_xml_value() -> None:
    assert FileType.xml == "xml"
