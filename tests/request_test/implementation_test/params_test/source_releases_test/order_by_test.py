import pytest

from fred.request.implementation.params.source_releases.order_by import OrderBy


@pytest.mark.contract_test
def test_release_id_value() -> None:
    assert OrderBy.release_id == "release_id"


@pytest.mark.contract_test
def test_name_value() -> None:
    assert OrderBy.name == "name"


@pytest.mark.contract_test
def test_press_release_value() -> None:
    assert OrderBy.press_release == "press_release"


@pytest.mark.contract_test
def test_realtime_start_value() -> None:
    assert OrderBy.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_realtime_end_value() -> None:
    assert OrderBy.realtime_end == "realtime_end"
