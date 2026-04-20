import pytest

from fred.enums.seasonal_adjustment_short import SeasonalAdjustmentShort


@pytest.mark.contract_test
def test_nsa_value() -> None:
    assert SeasonalAdjustmentShort.nsa == "NSA"


@pytest.mark.contract_test
def test_sa_value() -> None:
    assert SeasonalAdjustmentShort.sa == "SA"


@pytest.mark.contract_test
def test_saar_value() -> None:
    assert SeasonalAdjustmentShort.saar == "SAAR"
