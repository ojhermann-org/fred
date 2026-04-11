import pytest

from fred.enums.filter_variable import CategorySeries, ReleaseSeries


@pytest.mark.contract_test
def test_category_series_frequency_value() -> None:
    assert CategorySeries.frequency == "frequency"


@pytest.mark.contract_test
def test_category_series_units_value() -> None:
    assert CategorySeries.units == "units"


@pytest.mark.contract_test
def test_category_series_seasonal_adjustment_value() -> None:
    assert CategorySeries.seasonal_adjustment == "seasonal_adjustment"


@pytest.mark.contract_test
def test_release_series_frequency_value() -> None:
    assert ReleaseSeries.frequency == "frequency"


@pytest.mark.contract_test
def test_release_series_units_value() -> None:
    assert ReleaseSeries.units == "units"


@pytest.mark.contract_test
def test_release_series_seasonal_adjustment_value() -> None:
    assert ReleaseSeries.seasonal_adjustment == "seasonal_adjustment"
