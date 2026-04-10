from pydantic import ValidationError
import pytest

from fred.response.source import Source, SourceResponse


@pytest.mark.unit_test
def test_source_accepts_all_fields() -> None:
    source = Source(
        id=1,
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        name="Board of Governors of the Federal Reserve System",
        link="http://www.federalreserve.gov/",
    )
    assert source.id == 1
    assert source.name == "Board of Governors of the Federal Reserve System"
    assert source.link == "http://www.federalreserve.gov/"


@pytest.mark.unit_test
def test_source_link_is_optional() -> None:
    source = Source(
        id=1,
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        name="Board of Governors of the Federal Reserve System",
    )
    assert source.link is None


@pytest.mark.unit_test
def test_source_raises_on_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        Source(
            id=1,
            realtime_start="not-a-date",
            realtime_end="2013-08-14",
            name="Board of Governors of the Federal Reserve System",
        )


@pytest.mark.unit_test
def test_source_raises_on_invalid_realtime_end() -> None:
    with pytest.raises(ValidationError):
        Source(
            id=1,
            realtime_start="2013-08-14",
            realtime_end="not-a-date",
            name="Board of Governors of the Federal Reserve System",
        )


@pytest.mark.unit_test
def test_source_response_accepts_valid_payload() -> None:
    response = SourceResponse(
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        sources=[
            Source(
                id=1,
                realtime_start="2013-08-14",
                realtime_end="2013-08-14",
                name="Board of Governors of the Federal Reserve System",
                link="http://www.federalreserve.gov/",
            )
        ],
    )
    assert len(response.sources) == 1
    assert response.sources[0].id == 1


@pytest.mark.unit_test
def test_source_response_accepts_empty_sources() -> None:
    response = SourceResponse(
        realtime_start="2013-08-14",
        realtime_end="2013-08-14",
        sources=[],
    )
    assert response.sources == []


@pytest.mark.unit_test
def test_source_response_raises_on_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        SourceResponse(
            realtime_start="not-a-date",
            realtime_end="2013-08-14",
            sources=[],
        )
