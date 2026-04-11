import pytest

from fred.enums.output_type import OutputType


@pytest.mark.contract_test
def test_obs_by_real_time_period_value() -> None:
    assert OutputType.obs_by_real_time_period == 1


@pytest.mark.contract_test
def test_obs_by_vintage_date_all_value() -> None:
    assert OutputType.obs_by_vintage_date_all == 2


@pytest.mark.contract_test
def test_obs_by_vintage_date_new_and_revised_value() -> None:
    assert OutputType.obs_by_vintage_date_new_and_revised == 3


@pytest.mark.contract_test
def test_obs_initial_release_value() -> None:
    assert OutputType.obs_initial_release == 4
