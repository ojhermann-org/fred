from enum import StrEnum


def combine(base: str, *args: str | None) -> str:
    return base + "".join(["/" + a for a in args if a is not None])


ENDPOINT_BASE: str = "https://api.stlouisfed.org/fred"


class Base(StrEnum):
    category = combine(ENDPOINT_BASE, "category")
    release = combine(ENDPOINT_BASE, "release")
    releases = combine(ENDPOINT_BASE, "releases")
    series = combine(ENDPOINT_BASE, "series")
    source = combine(ENDPOINT_BASE, "source")
    sources = combine(ENDPOINT_BASE, "sources")
    tags = combine(ENDPOINT_BASE, "tags")
    tags_related = combine(ENDPOINT_BASE, "related_tags")


class Endpoint(StrEnum):
    category = Base.category
    category_children = combine(Base.category, "children")
    category_related = combine(Base.category, "related")
    category_series = combine(Base.category, "series")
    category_tags = combine(Base.category, "tags")
    category_related_tags = combine(Base.category, "related_tags")
    release = Base.release
    release_dates = combine(Base.release, "dates")
    release_series = combine(Base.release, "series")
    release_sources = combine(Base.release, "sources")
    release_related_tags = combine(Base.release, "related_tags")
    release_tables = combine(Base.release, "tables")
    release_tags = combine(Base.release, "tags")
    releases = Base.releases
    releases_dates = combine(Base.releases, "dates")
    series = Base.series
    series_categories = combine(Base.series, "categories")
    series_observations = combine(Base.series, "observations")
    series_release = combine(Base.series, "release")
    series_search = combine(Base.series, "search")
    series_search_tags = combine(Base.series, "search", "tags")
    series_search_related_tags = combine(Base.series, "search", "related_tags")
    series_tags = combine(Base.series, "tags")
    series_updates = combine(Base.series, "updates")
    series_vintagedates = combine(Base.series, "vintagedates")
    source = Base.source
    source_releases = combine(Base.source, "releases")
    sources = Base.sources
    tags = Base.tags
    tags_related = Base.tags_related
    tags_series = combine(Base.tags, "series")
