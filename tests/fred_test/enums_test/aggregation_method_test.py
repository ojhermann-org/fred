import pytest

from fred.enums.aggregation_method import AggregationMethod


@pytest.mark.contract_test
def test_average_value() -> None:
    assert AggregationMethod.average == "avg"


@pytest.mark.contract_test
def test_sum_value() -> None:
    assert AggregationMethod.sum == "sum"


@pytest.mark.contract_test
def test_end_of_period_value() -> None:
    assert AggregationMethod.end_of_period == "eop"
