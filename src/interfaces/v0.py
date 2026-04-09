from enum import StrEnum
from typing import Protocol


class Endpoint(StrEnum): ...


class Request(Protocol):
    def endpoint(self) -> Endpoint: ...

    def parameters(self) -> dict[str, str]: ...


class Builder(Protocol):
    def build(self) -> Request: ...
