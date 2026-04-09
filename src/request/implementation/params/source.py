from pydantic import BaseModel, Field

from request.implementation.api_key import ApiKey
from request.implementation.file_type import FileType
from request.implementation.realtime import Realtime, today_st_louis


class Params(BaseModel):
    api_key: ApiKey = Field(...)

    file_type: FileType = Field(...)

    realtime_end: Realtime = Field(default_factory=today_st_louis)

    realtime_start: Realtime = Field(default_factory=today_st_louis)

    source_id: int = Field(..., gt=0)

    def for_request(self) -> dict[str, str]:
        return {k: str(v) for k, v in self.model_dump().items() if v is not None}
