from pydantic import BaseModel

from fred.types.realtime import Realtime


class Release(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
    press_release: bool
    link: str | None = None
    notes: str | None = None
