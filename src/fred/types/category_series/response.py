from pydantic import BaseModel, Field

from fred.enums import SeasonalAdjustment, SeasonalAdjustmentShort, SortOrder
from fred.enums.order_by import CategorySeries as OrderBy
from fred.types.last_updated import LastUpdated
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime


class CategorySeries(BaseModel):
    id: str
    realtime_start: Realtime
    realtime_end: Realtime
    title: str
    observation_start: Realtime
    observation_end: Realtime
    frequency: str
    frequency_short: str
    units: str
    units_short: str
    seasonal_adjustment: SeasonalAdjustment
    seasonal_adjustment_short: SeasonalAdjustmentShort
    last_updated: LastUpdated
    popularity: int
    group_popularity: int
    notes: str | None = None


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    series: list[CategorySeries] = Field(alias="seriess")
