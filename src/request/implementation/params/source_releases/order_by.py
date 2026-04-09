from enum import StrEnum, auto


class OrderBy(StrEnum):
    release_id = auto()
    name = auto()
    press_release = auto()
    realtime_start = auto()
    realtime_end = auto()
