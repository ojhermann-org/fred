from pydantic import BaseModel

from fred.types.realtime import Realtime


class Series(BaseModel):
    id: str
    realtime_start: Realtime
    realtime_end: Realtime
    title: str
    observation_start: str
    observation_end: str
    frequency: str
    frequency_short: str
    units: str
    units_short: str
    seasonal_adjustment: str
    seasonal_adjustment_short: str
    last_updated: str
    popularity: int
    group_popularity: int | None = None
    notes: str | None = None
