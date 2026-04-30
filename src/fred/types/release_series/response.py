from pydantic import BaseModel, Field

from fred.enums import SortOrder
from fred.enums.order_by import ReleaseSeries as OrderBy
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.release_series.series import Series


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    series: list[Series] = Field(alias="seriess")
