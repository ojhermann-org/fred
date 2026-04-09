from request.implementation.builder.source import Builder as Source
from request.interface.builder import Builder


class RequestBuilder:
    @staticmethod
    def source() -> type[Builder]:
        return Source
