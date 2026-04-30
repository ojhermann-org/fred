from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.category.category import Category
from fred.types.realtime import Realtime
from fred.types.series_categories.request_params import RequestParams
from fred.types.series_categories.response import Response
from fred.types.series_id import SeriesId

ENDPOINT = Endpoint.series_categories

__all__ = [
    "ApiKey",
    "Category",
    "ENDPOINT",
    "FileType",
    "Realtime",
    "RequestParams",
    "Response",
    "SeriesId",
]
