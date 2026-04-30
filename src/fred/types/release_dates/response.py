from pydantic import BaseModel

from fred.enums import SortOrder
from fred.enums.order_by import ReleaseDates as OrderBy
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.release_dates.release_date import ReleaseDate

Limit = int


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    release_dates: list[ReleaseDate]
