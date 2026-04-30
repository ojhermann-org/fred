from enum import StrEnum, auto


class CategorySeries(StrEnum):
    frequency = auto()
    units = auto()
    seasonal_adjustment = auto()


class ReleaseSeries(StrEnum):
    frequency = auto()
    units = auto()
    seasonal_adjustment = auto()


class SeriesSearch(StrEnum):
    frequency = auto()
    units = auto()
    seasonal_adjustment = auto()
