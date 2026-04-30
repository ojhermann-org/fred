from pydantic import BaseModel

from fred.types.realtime import Realtime


class ReleaseDate(BaseModel):
    release_id: int
    date: Realtime
