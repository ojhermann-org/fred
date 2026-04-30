from pydantic import BaseModel, Field

from fred.enums.aggregation_method import AggregationMethod
from fred.enums.frequency import Frequency
from fred.enums.output_type import OutputType
from fred.enums.sort_order import SortOrder
from fred.enums.units import Units
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.series_id import SeriesId
from fred.types.series_observations.file_type import FileType
from fred.types.series_observations.limit import Limit


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    series_id: SeriesId = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    limit: Limit = Field(default=100000)
    offset: Offset = Field(default=0)
    sort_order: SortOrder = Field(default=SortOrder.asc)
    observation_start: str = Field(default="1776-07-04")
    observation_end: str = Field(default="9999-12-31")
    units: Units = Field(default=Units.levels)
    frequency: Frequency | None = Field(default=None)
    aggregation_method: AggregationMethod | None = Field(default=None)
    output_type: OutputType = Field(default=OutputType.obs_by_real_time_period)
    vintage_date: str | None = Field(default=None)
