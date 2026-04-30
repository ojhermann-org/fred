from __future__ import annotations

from pydantic import BaseModel


class Element(BaseModel):
    element_id: int
    release_id: int
    series_id: str | None = None
    parent_id: int
    line: str
    type: str
    name: str
    level: str
    children: list[Element] = []


Element.model_rebuild()
