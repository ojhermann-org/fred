import re
from typing import Annotated

from pydantic import BeforeValidator


def validate_semicolon_separated(v: str) -> str:
    if not re.fullmatch(r"[^\s;:]+(?:;[^\s;:]+)*", v):
        raise ValueError("must be non-whitespace strings separated by semicolons")
    return v


type TagNames = Annotated[
    str | None,
    BeforeValidator(lambda v: v if v is None else validate_semicolon_separated(v)),
]
