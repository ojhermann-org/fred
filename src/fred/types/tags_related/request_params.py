from pydantic import BaseModel, Field

from fred.enums import SortOrder, TagGroupID
from fred.enums.file_type import FileType
from fred.enums.order_by import RelatedTags as OrderBy
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.category_tags.tag_names import TagNames
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    tag_names: TagNames = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    exclude_tag_names: TagNames = Field(default=None)
    tag_group_id: TagGroupID | None = Field(default=None)
    search_text: str | None = Field(default=None)
    limit: Limit = Field(default=1000)
    offset: Offset = Field(default=0)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.asc)
