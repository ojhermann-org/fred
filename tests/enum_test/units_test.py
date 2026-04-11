import pytest

from fred.enums.units import Units


@pytest.mark.contract_test
def test_levels_value() -> None:
    assert Units.levels == "lin"


@pytest.mark.contract_test
def test_change_value() -> None:
    assert Units.change == "chg"


@pytest.mark.contract_test
def test_change_from_one_year_ago_value() -> None:
    assert Units.change_from_one_year_ago == "ch1"


@pytest.mark.contract_test
def test_percent_change_value() -> None:
    assert Units.percent_change == "pch"


@pytest.mark.contract_test
def test_percent_change_from_one_year_ago_value() -> None:
    assert Units.percent_change_from_one_year_ago == "pc1"


@pytest.mark.contract_test
def test_compounded_annual_rate_of_change_value() -> None:
    assert Units.compounded_annual_rate_of_change == "pca"


@pytest.mark.contract_test
def test_continuously_compounded_rate_of_change_value() -> None:
    assert Units.continuously_compounded_rate_of_change == "cch"


@pytest.mark.contract_test
def test_continuously_compounded_annual_rate_of_change_value() -> None:
    assert Units.continuously_compounded_annual_rate_of_change == "cca"


@pytest.mark.contract_test
def test_natural_log_value() -> None:
    assert Units.natural_log == "log"
