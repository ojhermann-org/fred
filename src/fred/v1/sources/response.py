from pydantic import BaseModel

from fred.v1.realtime import Realtime
from fred.v1.sort_order import SortOrder
from fred.v1.source.response import Response as Source
from fred.v1.sources.order_by import OrderBy


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: int
    limit: int
    sources: list[Source]
