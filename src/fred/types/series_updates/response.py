from pydantic import BaseModel

from fred.enums.filter_value import SeriesUpdates as FilterValue
from fred.enums.sort_order import SortOrder
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.series.series import Series


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    filter_variable: str
    filter_value: FilterValue
    order_by: str
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    seriess: list[Series]
