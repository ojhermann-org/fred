from typing import Any

from geojson_pydantic import Feature, FeatureCollection
from geojson_pydantic.geometries import Geometry


class Response(FeatureCollection[Feature[Geometry, dict[str, Any]]]):
    name: str
    crs: dict[str, Any] | None = None
