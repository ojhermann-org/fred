from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime
from fred.types.series_id import SeriesId


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    series_id: SeriesId = Field(...)
    date: Realtime | None = Field(default=None)
    start_date: Realtime | None = Field(default=None)
