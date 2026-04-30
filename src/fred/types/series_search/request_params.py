from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.enums.filter_variable import SeriesSearch as FilterVariableSeriesSearch
from fred.enums.order_by import SeriesSearch as OrderBy
from fred.enums.search_type import SearchType
from fred.enums.sort_order import SortOrder
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.category_tags.tag_names import TagNames
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    search_text: str = Field(...)
    search_type: SearchType = Field(default=SearchType.full_text)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    limit: Limit = Field(default=1000)
    offset: Offset = Field(default=0)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.asc)
    filter_variable: FilterVariableSeriesSearch | None = Field(default=None)
    filter_value: str | None = Field(default=None)
    tag_names: TagNames = Field(default=None)
    exclude_tag_names: TagNames = Field(default=None)
