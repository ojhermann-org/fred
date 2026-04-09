from fred.request.implementation.builder.source import Builder as Source
from fred.request.interface.builder import Builder


class RequestBuilder:
    @staticmethod
    def source() -> type[Builder]:
        return Source
