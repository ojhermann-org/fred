from fred.enums.endpoint import Endpoint
from fred.enums.file_type import FileType
from fred.types.api_key import ApiKey
from fred.types.realtime import Realtime
from fred.types.release_id import ReleaseID
from fred.types.release_sources.request_params import RequestParams
from fred.types.release_sources.response import Response
from fred.types.release_sources.source import Source

ENDPOINT = Endpoint.release_sources

__all__ = [
    "ApiKey",
    "ENDPOINT",
    "FileType",
    "Realtime",
    "ReleaseID",
    "RequestParams",
    "Response",
    "Source",
]
