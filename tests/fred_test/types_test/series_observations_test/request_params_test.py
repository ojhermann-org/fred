from pydantic import ValidationError
import pytest

from fred.enums.aggregation_method import AggregationMethod
from fred.enums.frequency import Frequency
from fred.enums.output_type import OutputType
from fred.enums.sort_order import SortOrder
from fred.enums.units import Units
from fred.types.series_observations.file_type import FileType
from fred.types.series_observations.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SERIES_ID = "GNPCA"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
    )
    assert p.series_id == _VALID_SERIES_ID


@pytest.mark.contract_test
def test_limit_defaults_to_100000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.limit == 100000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_units_defaults_to_levels() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.units == Units.levels


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_accepts_xlsx_file_type() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.xlsx,
        series_id=_VALID_SERIES_ID,
    )
    assert p.file_type == FileType.xlsx


@pytest.mark.contract_test
def test_accepts_csv_file_type() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.csv,
        series_id=_VALID_SERIES_ID,
    )
    assert p.file_type == FileType.csv


@pytest.mark.contract_test
def test_rejects_limit_above_100000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            limit=100001,
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            series_id=_VALID_SERIES_ID,
            offset=-1,
        )


@pytest.mark.contract_test
def test_frequency_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.frequency is None


@pytest.mark.contract_test
def test_accepts_explicit_frequency() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
        frequency=Frequency.monthly,
    )
    assert p.frequency == Frequency.monthly


@pytest.mark.contract_test
def test_aggregation_method_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.aggregation_method is None


@pytest.mark.contract_test
def test_accepts_explicit_aggregation_method() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        series_id=_VALID_SERIES_ID,
        aggregation_method=AggregationMethod.average,
    )
    assert p.aggregation_method == AggregationMethod.average


@pytest.mark.contract_test
def test_output_type_defaults_to_obs_by_real_time_period() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.output_type == OutputType.obs_by_real_time_period


@pytest.mark.contract_test
def test_vintage_date_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, series_id=_VALID_SERIES_ID
    )
    assert p.vintage_date is None
