from pydantic import BaseModel

from fred.enums.sort_order import SortOrder
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.series_vintagedates.limit import Limit


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: str
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    vintage_dates: list[str]
