from pydantic import ValidationError
import pytest

from fred import geofred_shapes


def _valid_feature(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "type": "Feature",
        "properties": {"bea_region": 8, "bea_regi_1": "Far West"},
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": [[[[1485, 2651], [1482, 2635], [1458, 2688], [1485, 2651]]]],
        },
    }
    base.update(overrides)
    return base


def _valid_response(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "type": "FeatureCollection",
        "name": "state_bea_region",
        "crs": {
            "type": "name",
            "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"},
        },
        "features": [_valid_feature()],
    }
    base.update(overrides)
    return base


@pytest.mark.contract_test
def test_accepts_valid_response() -> None:
    r = geofred_shapes.Response.model_validate(_valid_response())
    assert r.type == "FeatureCollection"
    assert r.name == "state_bea_region"
    assert len(r.features) == 1
    geometry = r.features[0].geometry
    assert geometry is not None
    assert geometry.type == "MultiPolygon"
    assert r.features[0].properties == {"bea_region": 8, "bea_regi_1": "Far West"}


@pytest.mark.contract_test
def test_accepts_null_crs() -> None:
    r = geofred_shapes.Response.model_validate(_valid_response(crs=None))
    assert r.crs is None


@pytest.mark.contract_test
def test_accepts_empty_features() -> None:
    r = geofred_shapes.Response.model_validate(_valid_response(features=[]))
    assert r.features == []


@pytest.mark.contract_test
def test_accepts_point_geometry() -> None:
    r = geofred_shapes.Response.model_validate(
        _valid_response(
            features=[
                _valid_feature(geometry={"type": "Point", "coordinates": [100.0, 0.0]})
            ]
        )
    )
    geometry = r.features[0].geometry
    assert geometry is not None
    assert geometry.type == "Point"


@pytest.mark.contract_test
def test_accepts_null_properties() -> None:
    r = geofred_shapes.Response.model_validate(
        _valid_response(features=[_valid_feature(properties=None)])
    )
    assert r.features[0].properties is None


@pytest.mark.contract_test
def test_coerces_empty_list_properties_to_none() -> None:
    # FRED sends [] instead of null for features with no properties
    r = geofred_shapes.Response.model_validate(
        _valid_response(features=[_valid_feature(properties=[])])
    )
    assert r.features[0].properties is None


@pytest.mark.contract_test
def test_rejects_missing_name() -> None:
    with pytest.raises(ValidationError):
        data = _valid_response()
        del data["name"]  # type: ignore[attr-defined]
        geofred_shapes.Response.model_validate(data)


@pytest.mark.contract_test
def test_rejects_invalid_type() -> None:
    with pytest.raises(ValidationError):
        geofred_shapes.Response.model_validate(_valid_response(type="Feature"))
