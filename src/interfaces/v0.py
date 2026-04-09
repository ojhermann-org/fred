from enum import StrEnum
from typing import Protocol


class FredEndpoint(StrEnum): ...


class Request(Protocol):
    def parameters(self) -> dict[str, str]: ...

    def endpoint(self) -> FredEndpoint: ...


class RequestBuilder(Protocol):
    def build(self) -> Request: ...
