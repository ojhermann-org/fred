from enum import StrEnum, auto


class FileType(StrEnum):
    json = auto()
    xml = auto()
    xlsx = auto()
    csv = auto()
