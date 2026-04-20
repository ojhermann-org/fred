from datetime import datetime
import re
from typing import Annotated

from pydantic import AfterValidator

LAST_UPDATED_PATTERN = re.compile(
    r"^\d{4}-(0[1-9]|1[0-2])-\d{2} \d{2}:\d{2}:\d{2}[+-](0\d|1[0-4])$"  # offset 00–14 covers all real UTC offsets
)


def validate_last_updated(s: str) -> str:
    s = s.strip()
    if len(s) == 0:
        raise ValueError("Value cannot be empty")
    if not LAST_UPDATED_PATTERN.match(s):
        raise ValueError(
            "Value must be in YYYY-MM-DD HH:MM:SS±HH format"
        )  # datetime with timezone offset
    datetime.fromisoformat(
        s + ":00"
    )  # fromisoformat requires ±HH:MM offset before Python 3.11; appending ":00" normalizes ±HH to ±HH:MM
    return s


LastUpdated = Annotated[str, AfterValidator(validate_last_updated)]
