from pydantic import BaseModel

from fred.types.category import Category


class Response(BaseModel):
    categories: list[Category]
