from datetime import date
import re
from typing import Annotated

from pydantic import AfterValidator

_REALTIME_PATTERN = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-\d{2}$")


def validate_realtime(s: str) -> str:
    s = s.strip()
    if len(s) == 0:
        raise ValueError("Value cannot be empty")
    if not _REALTIME_PATTERN.match(s):
        raise ValueError("Value must be in YYYY-MM-DD format")
    date.fromisoformat(s)
    return s


Realtime = Annotated[str, AfterValidator(validate_realtime)]
