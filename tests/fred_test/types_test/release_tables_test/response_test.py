from pydantic import ValidationError
import pytest

from fred import release_tables


def _valid_element(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "element_id": 12887,
        "release_id": 53,
        "series_id": "DGDSRL1A225NBEA",
        "parent_id": 12886,
        "line": "3",
        "type": "series",
        "name": "Goods",
        "level": "1",
        "children": [],
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "name": "Personal consumption expenditures",
        "element_id": 12886,
        "release_id": "53",
        "elements": {"12887": _valid_element()},
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = release_tables.Response.model_validate(_valid_response())
    assert r.name == "Personal consumption expenditures"
    assert r.element_id == 12886
    assert r.release_id == "53"
    assert len(r.elements) == 1
    assert "12887" in r.elements


@pytest.mark.contract_test
def test_element_fields_parsed_correctly() -> None:
    r = release_tables.Response.model_validate(_valid_response())
    el = r.elements["12887"]
    assert el.element_id == 12887
    assert el.release_id == 53
    assert el.series_id == "DGDSRL1A225NBEA"
    assert el.parent_id == 12886
    assert el.line == "3"
    assert el.type == "series"
    assert el.name == "Goods"
    assert el.level == "1"
    assert el.children == []


@pytest.mark.contract_test
def test_accepts_multiple_elements() -> None:
    r = release_tables.Response.model_validate(
        _valid_response(
            elements={
                "12887": _valid_element(),
                "12890": _valid_element(element_id=12890, name="Services"),
            }
        )
    )
    assert len(r.elements) == 2
    assert r.elements["12890"].name == "Services"


@pytest.mark.contract_test
def test_element_series_id_can_be_none() -> None:
    r = release_tables.Response.model_validate(
        _valid_response(elements={"12887": _valid_element(series_id=None)})
    )
    assert r.elements["12887"].series_id is None


@pytest.mark.contract_test
def test_element_with_children() -> None:
    child = _valid_element(element_id=12888, parent_id=12887, name="Durable goods")
    parent = _valid_element(children=[child])
    r = release_tables.Response.model_validate(
        _valid_response(elements={"12887": parent})
    )
    assert len(r.elements["12887"].children) == 1
    assert r.elements["12887"].children[0].name == "Durable goods"


@pytest.mark.contract_test
def test_accepts_empty_elements_dict() -> None:
    r = release_tables.Response.model_validate(_valid_response(elements={}))
    assert r.elements == {}


@pytest.mark.contract_test
def test_rejects_missing_name() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["name"]
        release_tables.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_missing_elements() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["elements"]
        release_tables.Response.model_validate(data)
