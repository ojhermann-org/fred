from pydantic import BaseModel, Field

from request.implementation.api_key import ApiKey
from request.implementation.file_type import FileType
from request.implementation.params.sources.order_by import OrderBy
from request.implementation.realtime import Realtime, today_st_louis
from request.implementation.sort_order import SortOrder


class Params(BaseModel):
    api_key: ApiKey = Field(...)

    file_type: FileType = Field(...)

    realtime_start: Realtime = Field(default_factory=today_st_louis)

    realtime_end: Realtime = Field(default_factory=today_st_louis)

    limit: int = Field(default=1000, gt=0, lt=1001)

    offset: int = Field(default=0, gt=-1)

    order_by: OrderBy = Field(default=OrderBy.source_id)

    sort_order: SortOrder = Field(default=SortOrder.asc)

    def for_request(self) -> dict[str, str]:
        return {k: str(v) for k, v in self.model_dump().items() if v is not None}
