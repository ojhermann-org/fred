from typing import Self

from request.enum.endpoint import Endpoint
from request.implementation.api_key import ApiKey
from request.implementation.file_type import FileType
from request.implementation.params.source import Params
from request.implementation.realtime import Realtime, today_st_louis
from request.implementation.request import Request as RequestImplementation
from request.interface.request import Request


class Builder:
    def __init__(
        self,
        api_key: ApiKey,
        source_id: int,
        file_type: FileType = FileType.json,
    ) -> None:
        self._params: Params = Params(
            api_key=api_key,
            source_id=source_id,
            file_type=file_type,
            realtime_start=today_st_louis(),
            realtime_end=today_st_louis(),
        )

    def file_type(self, value: FileType) -> Self:
        self._params.file_type = value
        return self

    def realtime_start(self, value: Realtime) -> Self:
        self._params.realtime_start = value
        return self

    def realtime_end(self, value: Realtime) -> Self:
        self._params.realtime_end = value
        return self

    def build(self) -> Request:
        return RequestImplementation(
            endpoint=Endpoint.source, parameters=self._params.for_request()
        )
