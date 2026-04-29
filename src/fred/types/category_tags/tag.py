from pydantic import BaseModel

from fred.enums.tag_group_id import TagGroupID
from fred.types.fred_timestamp import FredTimestamp


class Tag(BaseModel):
    name: str
    group_id: TagGroupID
    notes: str
    created: FredTimestamp
    popularity: int
    series_count: int
