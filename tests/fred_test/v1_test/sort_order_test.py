import pytest

from fred.v1.sort_order import SortOrder


@pytest.mark.contract_test
def test_asc_value() -> None:
    assert SortOrder.asc == "asc"


@pytest.mark.contract_test
def test_desc_value() -> None:
    assert SortOrder.desc == "desc"
