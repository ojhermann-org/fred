from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime
from fred.types.series.request_params import RequestParams
from fred.types.series.response import Response
from fred.types.series.series import Series
from fred.types.series_id import SeriesId

ENDPOINT = Endpoint.series

__all__ = [
    "ApiKey",
    "ENDPOINT",
    "FileType",
    "Realtime",
    "RequestParams",
    "Response",
    "Series",
    "SeriesId",
]
