from datetime import datetime
from zoneinfo import ZoneInfo

from fred.types.realtime import Realtime

_ST_LOUIS_TZ = ZoneInfo("America/Chicago")


def today_st_louis() -> Realtime:
    return datetime.now(tz=_ST_LOUIS_TZ).date().isoformat()
