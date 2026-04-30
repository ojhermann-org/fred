from datetime import date, datetime
from zoneinfo import ZoneInfo

from fred.types.realtime import Realtime

_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


def first_day_of_year_st_louis() -> Realtime:
    year = datetime.now(tz=_ST_LOUIS_TZ).year
    return date(year, 1, 1).isoformat()
