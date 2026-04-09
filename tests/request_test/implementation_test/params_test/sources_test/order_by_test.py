import pytest

from fred.request.implementation.params.sources.order_by import OrderBy


@pytest.mark.contract_test
def test_name_value() -> None:
    assert OrderBy.name == "name"


@pytest.mark.contract_test
def test_realtime_end_value() -> None:
    assert OrderBy.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_realtime_start_value() -> None:
    assert OrderBy.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_source_id_value() -> None:
    assert OrderBy.source_id == "source_id"
