from typing import Protocol

from fred.request.interface.request import Request


class Builder(Protocol):
    def build(self) -> Request: ...
