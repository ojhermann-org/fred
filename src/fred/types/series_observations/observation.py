from pydantic import BaseModel

from fred.types.realtime import Realtime


class Observation(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    date: str
    value: str
