from pydantic import BaseModel, Field

from fred.enums import SortOrder
from fred.enums.file_type import FileType
from fred.enums.order_by import Releases as OrderBy
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    limit: Limit = Field(default=1000)
    offset: Offset = Field(default=0)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.asc)
