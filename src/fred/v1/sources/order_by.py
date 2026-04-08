from enum import StrEnum, auto


class OrderBy(StrEnum):
    name = auto()
    realtime_end = auto()
    realtime_start = auto()
    source_id = auto()
