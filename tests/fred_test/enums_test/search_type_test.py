import pytest

from fred.enums.search_type import SearchType


@pytest.mark.contract_test
def test_full_text_value() -> None:
    assert SearchType.full_text == "full_text"


@pytest.mark.contract_test
def test_series_id_value() -> None:
    assert SearchType.series_id == "series_id"
