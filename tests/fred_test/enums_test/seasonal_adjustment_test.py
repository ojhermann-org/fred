import pytest

from fred.enums.seasonal_adjustment import SeasonalAdjustment


@pytest.mark.contract_test
def test_yes_value() -> None:
    assert SeasonalAdjustment.yes == "Seasonally Adjusted"


@pytest.mark.contract_test
def test_no_value() -> None:
    assert SeasonalAdjustment.no == "Not Seasonally Adjusted"
