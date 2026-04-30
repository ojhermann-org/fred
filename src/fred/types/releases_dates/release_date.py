from pydantic import BaseModel

from fred.types.realtime import Realtime


class ReleaseDate(BaseModel):
    release_id: int
    release_name: str
    date: Realtime
