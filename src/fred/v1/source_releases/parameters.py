from datetime import date

from pydantic import BaseModel, Field

from fred.v1.api_key import ApiKey
from fred.v1.file_type import FileType
from fred.v1.realtime import Realtime
from fred.v1.sort_order import SortOrder
from fred.v1.source_releases.order_by import OrderBy


class Parameters(BaseModel):
    api_key: ApiKey = Field(...)

    source_id: int = Field(..., gt=0)

    file_type: FileType = Field(default=FileType.xml)

    realtime_start: Realtime = Field(default=date.today().isoformat())

    realtime_end: Realtime = Field(default=date.today().isoformat())

    limit: int = Field(default=1000, gt=0, lt=1001)

    offset: int = Field(default=0, gt=-1)

    order_by: OrderBy = Field(default=OrderBy.release_id)

    sort_order: SortOrder = Field(default=SortOrder.asc)
