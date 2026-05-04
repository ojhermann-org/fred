from pydantic import BaseModel

from fred.types.geofred_series_group.series_group import SeriesGroup


class Response(BaseModel):
    series_group: SeriesGroup
