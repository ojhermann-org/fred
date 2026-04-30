from typing import Annotated

from pydantic import BaseModel, Field

from fred.enums import SortOrder
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.release_id import ReleaseID

Limit = Annotated[int, Field(ge=1, le=10000)]


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    release_id: ReleaseID = Field(...)
    realtime_start: Realtime = Field(default="1776-07-04")
    realtime_end: Realtime = Field(default="9999-12-31")
    limit: Limit = Field(default=10000)
    offset: Offset = Field(default=0)
    sort_order: SortOrder = Field(default=SortOrder.asc)
    include_release_dates_with_no_data: bool = Field(default=False)
