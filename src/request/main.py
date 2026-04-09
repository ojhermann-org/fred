from request.implementation.builder.source import Builder as Source


class RequestBuilder:
    @staticmethod
    def source() -> type[Source]:
        return Source
