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
    source = Base.source
    source_releases = combine(Base.source, "releases")
    sources = Base.sources
