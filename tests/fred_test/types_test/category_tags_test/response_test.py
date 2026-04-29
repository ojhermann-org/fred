from pydantic import ValidationError
import pytest

from fred import category_tags
from fred.enums import SortOrder
from fred.enums.order_by import CategoryTags as OrderBy


def _valid_tag(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "bea",
        "group_id": "src",
        "notes": "U.S. Department of Commerce: Bureau of Economic Analysis",
        "created": "2012-02-27 10:18:19-06",
        "popularity": 87,
        "series_count": 24,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-13",
        "realtime_end": "2013-08-13",
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
    r = category_tags.Response.model_validate(_valid_response())
    assert r.realtime_start == "2013-08-13"
    assert r.realtime_end == "2013-08-13"
    assert r.order_by == OrderBy.series_count
    assert r.sort_order == SortOrder.desc
    assert r.count == 1
    assert r.offset == 0
    assert r.limit == 1000
    assert len(r.tags) == 1


@pytest.mark.contract_test
def test_accepts_multiple_tags() -> None:
    r = category_tags.Response.model_validate(
        _valid_response(
            tags=[_valid_tag(), _valid_tag(name="nation", group_id="geot")], count=2
        )
    )
    assert len(r.tags) == 2
    assert r.tags[1].group_id == "geot"


@pytest.mark.contract_test
def test_accepts_empty_tags_list() -> None:
    r = category_tags.Response.model_validate(_valid_response(tags=[], count=0))
    assert r.tags == []


@pytest.mark.contract_test
def test_accepts_unknown_group_id() -> None:
    r = category_tags.Response.model_validate(
        _valid_response(tags=[_valid_tag(group_id="cc")])
    )
    assert r.tags[0].group_id == "cc"


@pytest.mark.contract_test
def test_order_by_parsed_as_enum() -> None:
    r = category_tags.Response.model_validate(_valid_response(order_by="popularity"))
    assert r.order_by == OrderBy.popularity


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        category_tags.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_sort_order() -> None:
    with pytest.raises(ValidationError):
        category_tags.Response.model_validate(_valid_response(sort_order="invalid"))


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        category_tags.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )


@pytest.mark.contract_test
def test_rejects_missing_tags_field() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["tags"]
        category_tags.Response.model_validate(data)
