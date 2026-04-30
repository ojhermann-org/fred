from typing import Annotated

from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime
from fred.types.release_id import ReleaseID

ElementID = Annotated[int, Field(ge=1)]


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    release_id: ReleaseID = Field(...)
    element_id: ElementID | None = Field(default=None)
    include_observation_values: bool = Field(default=False)
    observation_date: Realtime = Field(default="9999-12-31")
