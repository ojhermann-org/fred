from enum import StrEnum, auto


class CategorySeries(StrEnum):
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


class CategoryTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class CategoryRelatedTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class Releases(StrEnum):
    release_id = auto()
    name = auto()
    press_release = auto()
    realtime_start = auto()
    realtime_end = auto()


class ReleaseDates(StrEnum):
    release_date = auto()


class ReleasesDates(StrEnum):
    release_date = auto()
    release_id = auto()
    release_name = auto()


class ReleaseSeries(StrEnum):
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


class ReleaseTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class ReleaseRelatedTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class SeriesSearchTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class SeriesSearchRelatedTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class SeriesTags(StrEnum):
    series_count = auto()
    popularity = auto()
    created = auto()
    name = auto()
    group_id = auto()


class SeriesSearch(StrEnum):
    search_rank = auto()
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
