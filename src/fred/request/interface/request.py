from typing import Protocol

from fred.request.enum.endpoint import Endpoint


class Request(Protocol):
    def endpoint(self) -> Endpoint: ...

    def parameters(self) -> dict[str, str]: ...
