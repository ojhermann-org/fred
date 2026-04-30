from pydantic import BaseModel, Field

from fred.enums import SortOrder
from fred.enums.file_type import FileType
from fred.enums.order_by import SeriesTags as OrderBy
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.category_tags.tag_names import TagNames
from fred.types.realtime import Realtime
from fred.types.series_id import SeriesId


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    series_id: SeriesId = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.asc)
    tag_names: TagNames = Field(default=None)
