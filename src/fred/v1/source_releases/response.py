from pydantic import BaseModel

from fred.v1.realtime import Realtime
from fred.v1.sort_order import SortOrder
from fred.v1.source_releases.order_by import OrderBy


class Release(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
    press_release: bool
    link: str | None = None
    notes: str | None = None


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: int
    limit: int
    releases: list[Release]
