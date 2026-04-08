from pydantic import BaseModel

from fred.v1.realtime import Realtime


class Response(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
    link: str | None = None
    notes: str | None = None
