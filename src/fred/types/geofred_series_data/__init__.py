from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.geofred_series_data.observation import Observation
from fred.types.geofred_series_data.request_params import RequestParams
from fred.types.geofred_series_data.response import Response
from fred.types.geofred_series_data.series_data import SeriesData
from fred.types.realtime import Realtime
from fred.types.series_id import SeriesId

ENDPOINT = Endpoint.geofred_series_data

__all__ = [
    "ApiKey",
    "ENDPOINT",
    "FileType",
    "Observation",
    "Realtime",
    "RequestParams",
    "Response",
    "SeriesData",
    "SeriesId",
]
