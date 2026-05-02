from pydantic import BaseModel

from fred.enums.order_by import SourceReleases as OrderBy
from fred.enums.sort_order import SortOrder
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.releases.release import Release


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    order_by: OrderBy
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: Limit
    releases: list[Release]
