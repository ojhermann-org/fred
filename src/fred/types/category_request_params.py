from pydantic import BaseModel, Field

from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.category_id import CategoryID


class CategoryRequestParams(BaseModel):
    api_key: ApiKey = Field(...)
    file_type: FileType = Field(...)
    category_id: CategoryID = Field(...)
