from pydantic import ValidationError
import pytest

from fred.v1.sort_order import SortOrder
from fred.v1.source_releases.order_by import OrderBy
from fred.v1.source_releases.response import Release, Response

VALID_RELEASE = {
    "id": 13,
    "realtime_start": "2013-08-14",
    "realtime_end": "2013-08-14",
    "name": "G.17 Industrial Production and Capacity Utilization",
    "press_release": True,
    "link": "http://www.federalreserve.gov/releases/g17/",
}

VALID_RESPONSE = {
    "realtime_start": "2013-08-14",
    "realtime_end": "2013-08-14",
    "order_by": "release_id",
    "sort_order": "asc",
    "count": 26,
    "offset": 0,
    "limit": 1000,
    "releases": [VALID_RELEASE],
}


# --- Release ---


@pytest.mark.unit_test
def test_release_requires_id() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "id"}
    with pytest.raises(ValidationError):
        Release(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_requires_realtime_start() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "realtime_start"}
    with pytest.raises(ValidationError):
        Release(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_requires_realtime_end() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "realtime_end"}
    with pytest.raises(ValidationError):
        Release(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_requires_name() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "name"}
    with pytest.raises(ValidationError):
        Release(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_requires_press_release() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "press_release"}
    with pytest.raises(ValidationError):
        Release(**data)  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_link_is_optional() -> None:
    data = {k: v for k, v in VALID_RELEASE.items() if k != "link"}
    assert Release(**data).link is None  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_notes_is_optional() -> None:
    assert Release(**VALID_RELEASE).notes is None  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_release_accepts_notes() -> None:
    release = Release(**VALID_RELEASE, notes="Some notes.")  # ty:ignore[invalid-argument-type]
    assert release.notes == "Some notes."


# --- Response ---


@pytest.mark.unit_test
def test_response_requires_realtime_start() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_start"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_realtime_end() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_end"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_order_by() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "order_by"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_sort_order() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "sort_order"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_count() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "count"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_offset() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "offset"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_limit() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "limit"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_requires_releases() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "releases"}
    with pytest.raises(ValidationError):
        Response(**data)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_parses_releases_as_list_of_release() -> None:
    response = Response(**VALID_RESPONSE)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]
    assert len(response.releases) == 1
    assert isinstance(response.releases[0], Release)


@pytest.mark.unit_test
def test_response_order_by_parsed_as_enum() -> None:
    assert Response(**VALID_RESPONSE).order_by == OrderBy.release_id  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_response_sort_order_parsed_as_enum() -> None:
    assert Response(**VALID_RESPONSE).sort_order == SortOrder.asc  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]


# --- contract: parse representative FRED demo response ---

# Covers: release with link and press_release=True, without link, with notes
_DEMO_RELEASES = [
    {
        "id": 13,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "G.17 Industrial Production and Capacity Utilization",
        "press_release": True,
        "link": "http://www.federalreserve.gov/releases/g17/",
    },
    {
        "id": 106,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "M2 Own Rate",
        "press_release": False,
    },
    {
        "id": 131,
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "name": "G.13 Selected Interest Rates",
        "press_release": True,
        "link": "http://federalreserve.gov/releases/g13/",
        "notes": "With the issue dated January 8, 2002 (containing data for December 2001), the Federal Reserve ceased publication of the monthly G.13 statistical release.",
    },
]


@pytest.mark.contract_test
def test_parses_demo_response() -> None:
    response = Response(
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        order_by="release_id",  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]
        sort_order="asc",  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]
        count=26,
        offset=0,
        limit=1000,
        releases=_DEMO_RELEASES,  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]
    )
    assert response.count == 26
    assert len(response.releases) == 3

    g17 = response.releases[0]
    assert g17.id == 13
    assert g17.press_release is True
    assert g17.link == "http://www.federalreserve.gov/releases/g17/"
    assert g17.notes is None

    m2 = response.releases[1]
    assert m2.id == 106
    assert m2.press_release is False
    assert m2.link is None
    assert m2.notes is None

    g13 = response.releases[2]
    assert g13.id == 131
    assert g13.press_release is True
    assert g13.link is not None
    assert g13.notes is not None
