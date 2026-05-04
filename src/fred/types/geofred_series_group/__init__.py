from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.geofred_series_group.request_params import RequestParams
from fred.types.geofred_series_group.response import Response
from fred.types.geofred_series_group.series_group import SeriesGroup
from fred.types.series_id import SeriesId

ENDPOINT = Endpoint.geofred_series_group

__all__ = [
    "ApiKey",
    "ENDPOINT",
    "FileType",
    "RequestParams",
    "Response",
    "SeriesGroup",
    "SeriesId",
]
