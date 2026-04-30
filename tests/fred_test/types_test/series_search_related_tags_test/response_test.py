from pydantic import ValidationError
import pytest

from fred import series_search_related_tags
from fred.enums.order_by import SeriesSearchRelatedTags as OrderBy
from fred.enums.sort_order import SortOrder


def _valid_tag(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "sa",
        "group_id": "seas",
        "notes": "",
        "created": "2012-02-27 10:18:19-06",
        "popularity": 62,
        "series_count": 33,
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
    r = series_search_related_tags.Response.model_validate(_valid_response())
    assert r.order_by == OrderBy.series_count
    assert r.sort_order == SortOrder.desc
    assert len(r.tags) == 1


@pytest.mark.contract_test
def test_accepts_empty_tags() -> None:
    r = series_search_related_tags.Response.model_validate(
        _valid_response(tags=[], count=0)
    )
    assert r.tags == []


@pytest.mark.contract_test
def test_rejects_missing_tags() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["tags"]
        series_search_related_tags.Response.model_validate(data)
