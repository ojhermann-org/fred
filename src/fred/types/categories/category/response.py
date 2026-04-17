from pydantic import BaseModel

from fred.types.categories.category.category import Category


class Response(BaseModel):
    categories: list[Category]
