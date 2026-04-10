from pydantic import BaseModel

from fred.response.realtime import Realtime


class Source(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
    link: str | None = None


class SourceResponse(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    sources: list[Source]
