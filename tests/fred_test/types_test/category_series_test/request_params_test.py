from pydantic import ValidationError
import pytest

from fred.enums import Frequency, SeasonalAdjustment, SortOrder, Units
from fred.enums.file_type import FileType
from fred.enums.filter_variable import CategorySeries as FilterVariable
from fred.enums.order_by import CategorySeries as OrderBy
from fred.types.category_series.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.category_id == 0


@pytest.mark.contract_test
def test_realtime_start_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.realtime_start is not None


@pytest.mark.contract_test
def test_realtime_end_defaults_to_today() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.realtime_end is not None


@pytest.mark.contract_test
def test_accepts_explicit_realtime_start() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        realtime_start="2020-01-01",
    )
    assert p.realtime_start == "2020-01-01"


@pytest.mark.contract_test
def test_accepts_explicit_realtime_end() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        realtime_end="2024-12-31",
    )
    assert p.realtime_end == "2024-12-31"


@pytest.mark.contract_test
def test_limit_defaults_to_1000() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.limit == 1000


@pytest.mark.contract_test
def test_offset_defaults_to_0() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.offset == 0


@pytest.mark.contract_test
def test_order_by_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.order_by is None


@pytest.mark.contract_test
def test_sort_order_defaults_to_asc() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.sort_order == SortOrder.asc


@pytest.mark.contract_test
def test_filter_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.filter_value is None


@pytest.mark.contract_test
def test_accepts_explicit_limit() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        limit=500,
    )
    assert p.limit == 500


@pytest.mark.contract_test
def test_accepts_explicit_offset() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        offset=100,
    )
    assert p.offset == 100


@pytest.mark.contract_test
def test_accepts_explicit_order_by() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        order_by=OrderBy.series_id,
    )
    assert p.order_by == OrderBy.series_id


@pytest.mark.contract_test
def test_accepts_explicit_sort_order() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        sort_order=SortOrder.desc,
    )
    assert p.sort_order == SortOrder.desc


@pytest.mark.contract_test
@pytest.mark.parametrize(
    "filter_value",
    [
        Frequency.annual,
        Units.levels,
        SeasonalAdjustment.yes,
    ],
)
def test_accepts_filter_values(
    filter_value: Frequency | Units | SeasonalAdjustment,
) -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        filter_value=filter_value,
    )
    assert p.filter_value == filter_value


@pytest.mark.contract_test
def test_filter_variable_is_none_when_filter_value_is_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
    )
    assert p.filter_variable is None


@pytest.mark.contract_test
def test_filter_variable_is_frequency_when_filter_value_is_frequency() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        filter_value=Frequency.annual,
    )
    assert p.filter_variable == FilterVariable.frequency


@pytest.mark.contract_test
def test_filter_variable_is_units_when_filter_value_is_units() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        filter_value=Units.levels,
    )
    assert p.filter_variable == FilterVariable.units


@pytest.mark.contract_test
def test_filter_variable_is_seasonal_adjustment_when_filter_value_is_seasonal_adjustment() -> (
    None
):
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        category_id=0,
        filter_value=SeasonalAdjustment.yes,
    )
    assert p.filter_variable == FilterVariable.seasonal_adjustment


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            file_type=FileType.json,
            category_id=0,
        )


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            category_id=0,
        )


@pytest.mark.contract_test
def test_rejects_missing_category_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
        )


@pytest.mark.contract_test
def test_rejects_negative_category_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=-1,
        )


@pytest.mark.contract_test
def test_rejects_limit_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=0,
            limit=0,
        )


@pytest.mark.contract_test
def test_rejects_limit_above_1000() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=0,
            limit=1001,
        )


@pytest.mark.contract_test
def test_rejects_negative_offset() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            category_id=0,
            offset=-1,
        )
