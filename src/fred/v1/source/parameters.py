from datetime import date

from pydantic import BaseModel, Field

from fred.v1.api_key import ApiKey
from fred.v1.file_type import FileType
from fred.v1.realtime import Realtime


class Parameters(BaseModel):
    api_key: ApiKey = Field(...)

    source_id: int = Field(..., gt=0)

    file_type: FileType = Field(default=FileType.xml)

    realtime_start: Realtime = Field(default=date.today().isoformat())

    realtime_end: Realtime = Field(default=date.today().isoformat())
