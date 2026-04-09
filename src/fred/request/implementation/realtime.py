from datetime import date, datetime
import re
from typing import Annotated
from zoneinfo import ZoneInfo

from pydantic import AfterValidator

_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


def today_st_louis() -> str:
    """
    - this function helps reduce the number of incidences of asking for data that is not yet available
      - FRED API is maintained by the Federal Reserve Bank of St. Louis and most data is from the US
      - setting the default date to the current day in St. Louis avoids issues like passing in today in UTC, which could be > today in St. Louis
    """
    return datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()


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
