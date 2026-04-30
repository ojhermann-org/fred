from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.enums.filter_value import SeriesUpdates as FilterValue
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
    filter_value: FilterValue = Field(default=FilterValue.all)
    start_time: str | None = Field(default=None)
    end_time: str | None = Field(default=None)
