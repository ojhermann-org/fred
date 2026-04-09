from enum import StrEnum


# todo unit tests
# - *args is None returns base
# - *args is singleton returns {base}/{singleton}
# - *args is "a", "b", "c" returns {baes}/a/b/c
def combine(base: str, *args: str | None) -> str:
    return base + "".join(["/" + a for a in args if a is not None])


ENDPOINT_BASE: str = "https://api.stlouisfed.org/fred"


# todo unit tests
# - make sure each value is unique
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
