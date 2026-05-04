from pydantic import ValidationError
import pytest

from fred.enums.aggregation_method import AggregationMethod
from fred.enums.file_type import FileType
from fred.enums.frequency import Frequency
from fred.enums.seasonal_adjustment_short import SeasonalAdjustmentShort
from fred.enums.shape import Shape
from fred.enums.units import Units
from fred.types.geofred_regional_data.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_SERIES_GROUP = "882"
_VALID_DATE = "2013-01-01"
_VALID_UNITS = "Dollars"


def _params(**overrides: object) -> RequestParams:
    base: dict[str, object] = {
        "api_key": _VALID_API_KEY,
        "file_type": FileType.json,
        "series_group": _VALID_SERIES_GROUP,
        "region_type": Shape.state,
        "date": _VALID_DATE,
        "season": SeasonalAdjustmentShort.nsa,
        "units": _VALID_UNITS,
        "frequency": Frequency.annual,
    }
    base.update(overrides)
    return RequestParams(**base)  # type: ignore[arg-type]  # ty: ignore[invalid-argument-type]


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = _params()
    assert p.api_key == _VALID_API_KEY
    assert p.series_group == _VALID_SERIES_GROUP
    assert p.region_type == Shape.state
    assert p.date == _VALID_DATE
    assert p.season == SeasonalAdjustmentShort.nsa
    assert p.units == _VALID_UNITS
    assert p.frequency == Frequency.annual
    assert p.start_date is None
    assert p.transformation is None
    assert p.aggregation_method is None


@pytest.mark.contract_test
def test_accepts_all_optional_params() -> None:
    p = _params(
        start_date="2010-01-01",
        transformation=Units.percent_change,
        aggregation_method=AggregationMethod.sum,
    )
    assert p.start_date == "2010-01-01"
    assert p.transformation == Units.percent_change
    assert p.aggregation_method == AggregationMethod.sum


@pytest.mark.contract_test
def test_accepts_ssa_season() -> None:
    p = _params(season=SeasonalAdjustmentShort.ssa)
    assert p.season == SeasonalAdjustmentShort.ssa


@pytest.mark.contract_test
def test_accepts_all_region_types() -> None:
    for shape in Shape:
        p = _params(region_type=shape)
        assert p.region_type == shape


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(  # type: ignore[call-arg]
            file_type=FileType.json,
            series_group=_VALID_SERIES_GROUP,
            region_type=Shape.state,
            date=_VALID_DATE,
            season=SeasonalAdjustmentShort.nsa,
            units=_VALID_UNITS,
            frequency=Frequency.annual,
        )


@pytest.mark.contract_test
def test_rejects_empty_series_group() -> None:
    with pytest.raises(ValidationError):
        _params(series_group="")


@pytest.mark.contract_test
def test_rejects_empty_units() -> None:
    with pytest.raises(ValidationError):
        _params(units="")


@pytest.mark.contract_test
def test_rejects_invalid_date() -> None:
    with pytest.raises(ValidationError):
        _params(date="not-a-date")


@pytest.mark.contract_test
def test_rejects_invalid_start_date() -> None:
    with pytest.raises(ValidationError):
        _params(start_date="not-a-date")


@pytest.mark.contract_test
def test_rejects_invalid_region_type() -> None:
    with pytest.raises(ValidationError):
        _params(region_type="bogus")


@pytest.mark.contract_test
def test_rejects_invalid_season() -> None:
    with pytest.raises(ValidationError):
        _params(season="NSAAR")
