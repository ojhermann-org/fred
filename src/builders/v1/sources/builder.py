from datetime import date

from builders.v1.request import Request

ENDPOINT = "https://api.stlouisfed.org/fred/sources"
from fred.v1.file_type import FileType
from fred.v1.sort_order import SortOrder
from fred.v1.sources.order_by import OrderBy
from fred.v1.sources.parameters import Parameters


class Builder:
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._file_type: FileType = FileType.xml
        self._realtime_start: str = date.today().isoformat()
        self._realtime_end: str = date.today().isoformat()
        self._limit: int = 1000
        self._offset: int = 0
        self._order_by: OrderBy = OrderBy.source_id
        self._sort_order: SortOrder = SortOrder.asc

    def with_file_type(self, file_type: FileType) -> "Builder":
        self._file_type = file_type
        return self

    def with_realtime_start(self, realtime_start: str) -> "Builder":
        self._realtime_start = realtime_start
        return self

    def with_realtime_end(self, realtime_end: str) -> "Builder":
        self._realtime_end = realtime_end
        return self

    def with_limit(self, limit: int) -> "Builder":
        self._limit = limit
        return self

    def with_offset(self, offset: int) -> "Builder":
        self._offset = offset
        return self

    def with_order_by(self, order_by: OrderBy) -> "Builder":
        self._order_by = order_by
        return self

    def with_sort_order(self, sort_order: SortOrder) -> "Builder":
        self._sort_order = sort_order
        return self

    def build(self) -> Request:
        p = Parameters(
            api_key=self._api_key,
            file_type=self._file_type,
            realtime_start=self._realtime_start,
            realtime_end=self._realtime_end,
            limit=self._limit,
            offset=self._offset,
            order_by=self._order_by,
            sort_order=self._sort_order,
        )
        return Request(
            url=ENDPOINT,
            params={
                "api_key": p.api_key,
                "file_type": p.file_type,
                "realtime_start": p.realtime_start,
                "realtime_end": p.realtime_end,
                "limit": str(p.limit),
                "offset": str(p.offset),
                "order_by": p.order_by,
                "sort_order": p.sort_order,
            },
        )
