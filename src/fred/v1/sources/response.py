from pydantic import BaseModel

from fred.v1.order_by import OrderBy
from fred.v1.realtime import Realtime
from fred.v1.sort_order import SortOrder


class Source(BaseModel):
    id: int
    realtime_start: Realtime
    realtime_end: Realtime
    name: str
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
    sources: list[Source]
