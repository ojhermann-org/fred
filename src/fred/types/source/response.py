from pydantic import BaseModel

from fred.types.realtime import Realtime
from fred.types.release_sources.source import Source


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    sources: list[Source]
