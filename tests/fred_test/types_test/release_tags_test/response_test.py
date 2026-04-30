from pydantic import ValidationError
import pytest

from fred import release_tags
from fred.enums import SortOrder
from fred.enums.order_by import ReleaseTags as OrderBy
from fred.enums.tag_group_id import TagGroupID


def _valid_tag(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "frb",
        "group_id": "src",
        "notes": "Board of Governors of the Federal Reserve System",
        "created": "2012-02-27 10:18:19-06",
        "popularity": 90,
        "series_count": 18,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "order_by": "series_count",
        "sort_order": "desc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "tags": [_valid_tag()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = release_tags.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-14"
    assert r.realtime_end == "2013-08-14"
    assert r.order_by == OrderBy.series_count
    assert r.sort_order == SortOrder.desc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 1000
    assert len(r.tags) == 1


@pytest.mark.contract_test
def test_accepts_multiple_tags() -> None:
    r = release_tags.Response.model_validate(
        _valid_response(
            tags=[_valid_tag(), _valid_tag(name="nation", group_id="geot")], count=2
        )
    )
    assert len(r.tags) == 2
    assert r.tags[1].group_id == TagGroupID.geot


@pytest.mark.contract_test
def test_accepts_empty_tags_list() -> None:
    r = release_tags.Response.model_validate(_valid_response(tags=[], count=0))
    assert r.tags == []


@pytest.mark.contract_test
def test_accepts_empty_string_notes() -> None:
    r = release_tags.Response.model_validate(
        _valid_response(tags=[_valid_tag(notes="")])
    )
    assert r.tags[0].notes == ""


@pytest.mark.contract_test
def test_order_by_parsed_as_enum() -> None:
    r = release_tags.Response.model_validate(_valid_response(order_by="popularity"))
    assert r.order_by == OrderBy.popularity


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        release_tags.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_sort_order() -> None:
    with pytest.raises(ValidationError):
        release_tags.Response.model_validate(_valid_response(sort_order="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        release_tags.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_tags_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["tags"]
        release_tags.Response.model_validate(data)
