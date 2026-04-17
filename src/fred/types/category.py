from pydantic import BaseModel

from fred.types.category_id import CategoryID


class Category(BaseModel):
    id: CategoryID
    name: str
    parent_id: CategoryID
