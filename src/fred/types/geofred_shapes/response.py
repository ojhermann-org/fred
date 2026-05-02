from typing import Any

from geojson_pydantic import Feature, FeatureCollection
from geojson_pydantic.geometries import Geometry
from pydantic import model_validator


class Response(FeatureCollection[Feature[Geometry, dict[str, Any]]]):
    name: str
    crs: dict[str, Any] | None = None

    @model_validator(mode="before")
    @classmethod
    def _coerce_list_properties(cls, data: Any) -> Any:  # noqa: ANN401
        # FRED sends [] instead of null for features with no properties
        if not isinstance(data, dict):
            return data
        features = data.get("features")
        if not isinstance(features, list):
            return data
        for feature in features:
            if isinstance(feature, dict) and isinstance(
                feature.get("properties"), list
            ):
                feature["properties"] = None
        return data
