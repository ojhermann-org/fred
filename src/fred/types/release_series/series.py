from pydantic import BaseModel

from fred.enums import SeasonalAdjustment, SeasonalAdjustmentShort
from fred.types.fred_timestamp import FredTimestamp
from fred.types.realtime import Realtime


class Series(BaseModel):
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
    last_updated: FredTimestamp
    popularity: int
    group_popularity: int
    notes: str | None = None
