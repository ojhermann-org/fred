from pydantic import BaseModel

from fred.types.fred_timestamp import FredTimestamp
from fred.types.realtime import Realtime


class CategorySeries(BaseModel):
    id: str
    realtime_start: Realtime
    realtime_end: Realtime
    title: str
    observation_start: Realtime
    observation_end: Realtime
    frequency: str  # todo make requests to see if matches with Frequency enum or something else
    frequency_short: str  # todo see frequency
    units: str  # to do see frequency
    units_short: str  # to do see frequency
    seasonal_adjustment: str  # to do see frequency
    seasonal_adjustment_short: str  # to do see frequency
    last_updated: FredTimestamp
    popularity: int
    group_popularity: int
    notes: str | None
