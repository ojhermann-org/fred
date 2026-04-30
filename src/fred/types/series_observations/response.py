from pydantic import BaseModel

from fred.enums.output_type import OutputType
from fred.enums.sort_order import SortOrder
from fred.types.offset import Offset
from fred.types.realtime import Realtime
from fred.types.series_observations.observation import Observation


class Response(BaseModel):
    realtime_start: Realtime
    realtime_end: Realtime
    observation_start: str
    observation_end: str
    units: str
    output_type: OutputType
    file_type: str
    order_by: str
    sort_order: SortOrder
    count: int
    offset: Offset
    limit: int
    observations: list[Observation]
