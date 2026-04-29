from enum import StrEnum, auto


class TagGroupID(StrEnum):
    freq = auto()  # Frequency
    gen = auto()  # General or Concept
    geo = auto()  # Geography
    geot = auto()  # Geography Type
    rls = auto()  # Release
    seas = auto()  # Seasonal Adjustment
    src = auto()  # Source
    cc = auto()  # Citation & Copyright
