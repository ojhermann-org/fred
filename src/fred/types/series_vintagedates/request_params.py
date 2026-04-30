from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.enums.sort_order import SortOrder
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.series_id import SeriesId
from fred.types.series_vintagedates.limit import Limit


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    series_id: SeriesId = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    limit: Limit = Field(default=10000)
    offset: Offset = Field(default=0)
    sort_order: SortOrder = Field(default=SortOrder.asc)
