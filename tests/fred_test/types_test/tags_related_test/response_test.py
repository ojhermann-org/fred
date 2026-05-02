from pydantic import ValidationError
import pytest

from fred import tags_related
from fred.enums.order_by import RelatedTags as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_tag(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "nation",
        "group_id": "geo",
        "notes": "",
        "created": "2012-02-27 10:18:19-06",
        "popularity": 100,
        "series_count": 12,
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "realtime_start": "2013-08-14",
        "realtime_end": "2013-08-14",
        "order_by": "series_count",
        "sort_order": "asc",
        "count": 1,
        "offset": 0,
        "limit": 1000,
        "tags": [_valid_tag()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = tags_related.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.series_count
    assert r.sort_order == SortOrder.asc
    assert len(r.tags) == 1
    assert r.tags[0].name == "nation"


@pytest.mark.contract_test
def test_accepts_null_notes() -> None:
    r = tags_related.Response.model_validate(
        _valid_response(tags=[_valid_tag(notes=None)])
    )
    assert r.tags[0].notes is None


@pytest.mark.contract_test
def test_accepts_empty_tags() -> None:
    r = tags_related.Response.model_validate(_valid_response(tags=[], count=0))
    assert r.tags == []


@pytest.mark.contract_test
def test_rejects_invalid_order_by() -> None:
    with pytest.raises(ValidationError):
        tags_related.Response.model_validate(_valid_response(order_by="invalid"))


@pytest.mark.contract_test
def test_rejects_missing_tags() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["tags"]
        tags_related.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_realtime_start() -> None:
    with pytest.raises(ValidationError):
        tags_related.Response.model_validate(
            _valid_response(realtime_start="not-a-date")
        )
