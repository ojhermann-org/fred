import pytest

from fred.enums.frequency import Frequency


@pytest.mark.contract_test
def test_daily_value() -> None:
    assert Frequency.daily == "d"


@pytest.mark.contract_test
def test_weekly_value() -> None:
    assert Frequency.weekly == "w"


@pytest.mark.contract_test
def test_biweekly_value() -> None:
    assert Frequency.biweekly == "bw"


@pytest.mark.contract_test
def test_monthly_value() -> None:
    assert Frequency.monthly == "m"


@pytest.mark.contract_test
def test_quarterly_value() -> None:
    assert Frequency.quarterly == "q"


@pytest.mark.contract_test
def test_semiannual_value() -> None:
    assert Frequency.semiannual == "sa"


@pytest.mark.contract_test
def test_annual_value() -> None:
    assert Frequency.annual == "a"


@pytest.mark.contract_test
def test_weekly_ending_friday_value() -> None:
    assert Frequency.weekly_ending_friday == "wef"


@pytest.mark.contract_test
def test_weekly_ending_thursday_value() -> None:
    assert Frequency.weekly_ending_thursday == "weth"


@pytest.mark.contract_test
def test_weekly_ending_wednesday_value() -> None:
    assert Frequency.weekly_ending_wednesday == "wew"


@pytest.mark.contract_test
def test_weekly_ending_tuesday_value() -> None:
    assert Frequency.weekly_ending_tuesday == "wetu"


@pytest.mark.contract_test
def test_weekly_ending_monday_value() -> None:
    assert Frequency.weekly_ending_monday == "wem"


@pytest.mark.contract_test
def test_weekly_ending_sunday_value() -> None:
    assert Frequency.weekly_ending_sunday == "wesu"


@pytest.mark.contract_test
def test_weekly_ending_saturday_value() -> None:
    assert Frequency.weekly_ending_saturday == "wesa"


@pytest.mark.contract_test
def test_biweekly_ending_wednesday_value() -> None:
    assert Frequency.biweekly_ending_wednesday == "bwew"


@pytest.mark.contract_test
def test_biweekly_ending_monday_value() -> None:
    assert Frequency.biweekly_ending_monday == "bwem"
