from enum import StrEnum, auto


class Shape(StrEnum):
    bea = auto()  # Bureau of Economic Analysis Region
    msa = auto()  # Metropolitan Statistical Area
    frb = auto()  # Federal Reserve Bank Districts
    necta = auto()  # New England City and Town Area
    state = auto()  # US States
    country = auto()  # Countries
    county = auto()  # US Counties
    censusregion = auto()  # US Census Regions
    censusdivision = auto()  # US Census Divisions
