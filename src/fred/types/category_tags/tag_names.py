from typing import Annotated

from pydantic import BeforeValidator


def validate_semicolon_separated(v: str) -> str:
    parts = v.split(";")
    if not parts or any(not p or p != p.strip() or ":" in p for p in parts):
        raise ValueError(
            "must be non-empty strings without leading/trailing whitespace, separated by semicolons"
        )
    return v


type TagNames = Annotated[
    str | None,
    BeforeValidator(lambda v: v if v is None else validate_semicolon_separated(v)),
]
