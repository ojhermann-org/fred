from pydantic import BaseModel, Field

from fred.enums.shape import Shape
from fred.types.api_key import ApiKey


class RequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    shape: Shape = Field(...)
