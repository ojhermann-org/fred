from pydantic import ValidationError
import pytest

from fred.v1.order_by import OrderBy
from fred.v1.sort_order import SortOrder
from fred.v1.sources.response import Response, Source

# --- fixtures ---

VALID_SOURCE = {
    "id": 1,
    "realtime_start": "2013-08-14",
    "realtime_end": "2013-08-14",
    "name": "Board of Governors of the Federal Reserve System",
    "link": "http://www.federalreserve.gov/",
}

VALID_RESPONSE = {
    "realtime_start": "2013-08-14",
    "realtime_end": "2013-08-14",
    "order_by": "source_id",
    "sort_order": "asc",
    "count": 58,
    "offset": 0,
    "limit": 1000,
    "sources": [VALID_SOURCE],
}

# --- Source ---


@pytest.mark.unit_test
def test_source_requires_id() -> None:
    data = {k: v for k, v in VALID_SOURCE.items() if k != "id"}
    with pytest.raises(ValidationError):
        Source(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_source_requires_realtime_start() -> None:
    data = {k: v for k, v in VALID_SOURCE.items() if k != "realtime_start"}
    with pytest.raises(ValidationError):
        Source(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_source_requires_realtime_end() -> None:
    data = {k: v for k, v in VALID_SOURCE.items() if k != "realtime_end"}
    with pytest.raises(ValidationError):
        Source(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_source_requires_name() -> None:
    data = {k: v for k, v in VALID_SOURCE.items() if k != "name"}
    with pytest.raises(ValidationError):
        Source(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_source_link_is_optional() -> None:
    data = {k: v for k, v in VALID_SOURCE.items() if k != "link"}
    source = Source(**data)  # ty:ignore[invalid-argument-type]
    assert source.link is None


@pytest.mark.unit_test
def test_source_notes_is_optional() -> None:
    source = Source(**VALID_SOURCE)  # ty:ignore[invalid-argument-type]
    assert source.notes is None


@pytest.mark.unit_test
def test_source_accepts_notes() -> None:
    source = Source(**VALID_SOURCE, notes="Some notes.")  # ty:ignore[invalid-argument-type]
    assert source.notes == "Some notes."


# --- Response ---


@pytest.mark.unit_test
def test_response_requires_realtime_start() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_start"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_realtime_end() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_end"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_order_by() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "order_by"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_sort_order() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "sort_order"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_count() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "count"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_offset() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "offset"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_limit() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "limit"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_sources() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "sources"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_parses_sources_as_list_of_source() -> None:
    response = Response(**VALID_RESPONSE)  # ty:ignore[invalid-argument-type]
    assert len(response.sources) == 1
    assert isinstance(response.sources[0], Source)


@pytest.mark.unit_test
def test_response_order_by_parsed_as_enum() -> None:
    assert Response(**VALID_RESPONSE).order_by == OrderBy.source_id  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_sort_order_parsed_as_enum() -> None:
    assert Response(**VALID_RESPONSE).sort_order == SortOrder.asc  # ty:ignore[invalid-argument-type]


# --- contract: parse representative FRED demo response ---

# Covers: source with link, source without link, source with notes
_DEMO_SOURCES = [
    {
        "id": 1,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "Board of Governors of the Federal Reserve System",
        "link": "http://www.federalreserve.gov/",
    },
    {
        "id": 37,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "Bank of Japan",
    },
    {
        "id": 60,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "International Monetary Fund",
        "link": "http://www.imf.org/external/index.htm",
        "notes": "The International Monetary Fund (IMF) is an organization of 187 countries, working to foster global monetary cooperation, secure financial stability, facilitate international trade, promote high employment and sustainable economic growth, and reduce poverty around the world.",
    },
]


@pytest.mark.contract_test
def test_parses_demo_response() -> None:
    response = Response(
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        order_by="source_id",  # ty:ignore[invalid-argument-type]
        sort_order="asc",  # ty:ignore[invalid-argument-type]
        count=58,
        offset=0,
        limit=1000,
        sources=_DEMO_SOURCES,  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]
    )
    assert response.count == 58
    assert len(response.sources) == 3

    fed = response.sources[0]
    assert fed.id == 1
    assert fed.link == "http://www.federalreserve.gov/"
    assert fed.notes is None

    boj = response.sources[1]
    assert boj.id == 37
    assert boj.link is None
    assert boj.notes is None

    imf = response.sources[2]
    assert imf.id == 60
    assert imf.link == "http://www.imf.org/external/index.htm"
    assert imf.notes is not None
