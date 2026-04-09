from pydantic import ValidationError
import pytest

from fred.v1.source.response import Response

VALID_RESPONSE = {
    "id": 1,
    "realtime_start": "2013-08-14",
    "realtime_end": "2013-08-14",
    "name": "Board of Governors of the Federal Reserve System",
    "link": "http://www.federalreserve.gov/",
}


# required fields


@pytest.mark.unit_test
def test_requires_id() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "id"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty: ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_requires_realtime_start() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_start"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty: ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_requires_realtime_end() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "realtime_end"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty: ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_requires_name() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "name"}
    with pytest.raises(ValidationError):
        Response(**data)  # ty: ignore[invalid-argument-type]


# optional fields


@pytest.mark.unit_test
def test_link_is_optional() -> None:
    data = {k: v for k, v in VALID_RESPONSE.items() if k != "link"}
    assert Response(**data).link is None  # ty: ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_notes_is_optional() -> None:
    assert Response(**VALID_RESPONSE).notes is None  # ty: ignore[invalid-argument-type]


@pytest.mark.unit_test
def test_accepts_notes() -> None:
    response = Response(**VALID_RESPONSE, notes="Some notes.")  # ty: ignore[invalid-argument-type]
    assert response.notes == "Some notes."


# contract: representative sources from FRED demo data


@pytest.mark.contract_test
def test_parses_source_with_link() -> None:
    response = Response(**VALID_RESPONSE)  # ty: ignore[invalid-argument-type]
    assert response.id == 1
    assert response.name == "Board of Governors of the Federal Reserve System"
    assert response.link == "http://www.federalreserve.gov/"
    assert response.notes is None


@pytest.mark.contract_test
def test_parses_source_without_link() -> None:
    response = Response(
        id=37,
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        name="Bank of Japan",
    )
    assert response.id == 37
    assert response.link is None
    assert response.notes is None


@pytest.mark.contract_test
def test_parses_source_with_notes() -> None:
    response = Response(
        id=60,
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        name="International Monetary Fund",
        link="http://www.imf.org/external/index.htm",
        notes="The International Monetary Fund (IMF) is an organization of 187 countries, working to foster global monetary cooperation, secure financial stability, facilitate international trade, promote high employment and sustainable economic growth, and reduce poverty around the world.",
    )
    assert response.id == 60
    assert response.link is not None
    assert response.notes is not None
