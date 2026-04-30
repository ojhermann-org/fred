from pydantic import BaseModel

from fred.types.release_tables.element import Element


class Response(BaseModel):
    name: str
    element_id: int
    release_id: str
    elements: dict[str, Element]
