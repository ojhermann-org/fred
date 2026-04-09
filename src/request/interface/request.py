from typing import Protocol

from request.enum.endpoint import Endpoint


class Request(Protocol):
    def endpoint(self) -> Endpoint: ...

    def parameters(self) -> dict[str, str]: ...
