from fred.enums.endpoint import Endpoint
from fred.types.category_series.request_params import (
    ApiKey,
    CategoryID,
    FileType,
    Realtime,
    RequestParams,
)
from fred.types.category_series.response import Response

ENDPOINT = Endpoint.category_series

__all__ = [
    "ApiKey",
    "CategoryID",
    "ENDPOINT",
    "FileType",
    "Realtime",
    "RequestParams",
    "Response",
]
