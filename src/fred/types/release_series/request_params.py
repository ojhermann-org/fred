from typing import Self

from pydantic import BaseModel, Field, model_validator

from fred.enums import Frequency, SeasonalAdjustment, SortOrder, Units
from fred.enums.file_type import FileType
from fred.enums.filter_variable import ReleaseSeries as FilterVariable
from fred.enums.order_by import ReleaseSeries as OrderBy
from fred.functions.today_st_louis import today_st_louis
from fred.types.api_key import ApiKey
from fred.types.category_tags.tag_names import TagNames
from fred.types.limit import Limit
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.release_id import ReleaseID


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    release_id: ReleaseID = Field(...)
    realtime_start: Realtime = Field(default_factory=today_st_louis)
    realtime_end: Realtime = Field(default_factory=today_st_louis)
    limit: Limit = Field(default=1000)
    offset: Offset = Field(default=0)
    order_by: OrderBy | None = Field(default=None)
    sort_order: SortOrder = Field(default=SortOrder.asc)
    filter_value: Frequency | Units | SeasonalAdjustment | None = Field(default=None)
    filter_variable: FilterVariable | None = Field(default=None)
    tag_names: TagNames = Field(default=None)
    exclude_tag_names: TagNames = Field(default=None)

    @model_validator(mode="after")
    def set_filter_variable(self) -> Self:
        match self.filter_value:
            case Frequency():
                self.filter_variable = FilterVariable.frequency
            case Units():
                self.filter_variable = FilterVariable.units
            case SeasonalAdjustment():
                self.filter_variable = FilterVariable.seasonal_adjustment
            case _:
                self.filter_variable = None
        return self
