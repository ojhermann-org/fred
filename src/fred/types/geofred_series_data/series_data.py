from pydantic import BaseModel

from fred.types.geofred_series_data.observation import Observation


class SeriesData(BaseModel):
    title: str
    region: str
    seasonality: str
    units: str
    frequency: str
    data: dict[str, list[Observation]] | None = None
