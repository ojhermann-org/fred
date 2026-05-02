from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime
from fred.types.source_id import SourceId


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    source_id: SourceId = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
