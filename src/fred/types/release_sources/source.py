from pydantic import BaseModel

from fred.types.realtime import Realtime


class Source(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
    link: str | None = None
    notes: str | None = None
