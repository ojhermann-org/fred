from pydantic import BaseModel, Field

from fred.enums import SortOrder
from fred.enums.file_type import FileType
from fred.enums.order_by import ReleasesDates as OrderBy
from fred.functions.first_day_of_year_st_louis import first_day_of_year_st_louis
from fred.types.api_key import ApiKey
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    realtime_start: Realtime = Field(default_factory=first_day_of_year_st_louis)
    realtime_end: Realtime = Field(default="9999-12-31")
    limit: Limit = Field(default=1000)
    offset: Offset = Field(default=0)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.desc)
    include_release_dates_with_no_data: bool = Field(default=False)
