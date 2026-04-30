from pydantic import BaseModel

from fred.types.realtime import Realtime
from fred.types.series.series import Series


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    seriess: list[Series]
