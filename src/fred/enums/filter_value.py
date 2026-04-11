from enum import StrEnum, auto


class CategorySeries(StrEnum):
    # see filter_variable
    ...


class ReleaseSeries(StrEnum):
    # see filter_variable
    ...


class SeriesUpdates(StrEnum):
    macro = auto()
    regional = auto()
    all = auto()


class Sources(StrEnum):
    source_id = auto()
    name = auto()
    realtime_start = auto()
    realtime_end = auto()


class SourceReleases(StrEnum):
    release_id = auto()
    name = auto()
    press_release = auto()
    realtime_start = auto()
    realtime_end = auto()


class Tags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class TagsSeries(StrEnum):
    series_id = auto()
    title = auto()
    units = auto()
    frequency = auto()
    seasonal_adjustment = auto()
    realtime_start = auto()
    realtime_end = auto()
    last_updated = auto()
    observation_start = auto()
    observation_end = auto()
    popularity = auto()
    group_popularity = auto()
