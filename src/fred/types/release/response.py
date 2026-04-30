from pydantic import BaseModel

from fred.types.realtime import Realtime
from fred.types.releases.release import Release


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    releases: list[Release]
