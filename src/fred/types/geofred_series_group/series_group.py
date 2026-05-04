from pydantic import BaseModel

from fred.types.realtime import Realtime


class SeriesGroup(BaseModel):
    title: str
    region_type: str
    series_group: str
    season: str
    units: str
    frequency: str
    min_date: Realtime
    max_date: Realtime
