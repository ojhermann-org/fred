from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import TypeAdapter
import pytest

from fred.functions.today_st_louis import today_st_louis
from fred.types.realtime import Realtime

_adapter = TypeAdapter(Realtime)


@pytest.mark.unit_test
def test_returns_realtime() -> None:
    _adapter.validate_python(today_st_louis())


@pytest.mark.contract_test
def test_matches_st_louis_time() -> None:
    # there could be a race condition when these straddle midnight
    assert (
        today_st_louis()
        == datetime.now(tz=ZoneInfo("America/Chicago")).date().isoformat()
    )
