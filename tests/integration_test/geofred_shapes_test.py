import pytest

from fred import for_request, geofred_shapes
from tests.integration_test.conftest import FredGetJson


@pytest.mark.integration_test
def test_geofred_shapes_bea(api_key: str, fred_get_json: FredGetJson) -> None:
    params = geofred_shapes.RequestParams(
        api_key=api_key,
        shape=geofred_shapes.Shape.bea,
    )
    data = fred_get_json(str(geofred_shapes.ENDPOINT), for_request(params))
    response = geofred_shapes.Response.model_validate(data)
    assert response.type == "FeatureCollection"
    assert len(response.features) >= 1
