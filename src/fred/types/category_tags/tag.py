from pydantic import BaseModel

from fred.types.fred_timestamp import FredTimestamp


class Tag(BaseModel):
    name: str
    group_id: str
    notes: str | None
    created: FredTimestamp
    popularity: int
    series_count: int
