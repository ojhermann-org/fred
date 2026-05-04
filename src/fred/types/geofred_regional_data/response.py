from pydantic import BaseModel

from fred.types.geofred_series_data.series_data import SeriesData


class Response(BaseModel):
    meta: SeriesData
