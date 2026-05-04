from pydantic import BaseModel, Field

from fred.enums.aggregation_method import AggregationMethod
from fred.enums.file_type import FileType
from fred.enums.frequency import Frequency
from fred.enums.seasonal_adjustment_short import SeasonalAdjustmentShort
from fred.enums.shape import Shape
from fred.enums.units import Units
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    series_group: str = Field(..., min_length=1)
    region_type: Shape = Field(...)
    date: Realtime = Field(...)
    season: SeasonalAdjustmentShort = Field(...)
    units: str = Field(..., min_length=1)
    frequency: Frequency = Field(...)
    start_date: Realtime | None = Field(default=None)
    transformation: Units | None = Field(default=None)
    aggregation_method: AggregationMethod | None = Field(default=None)
