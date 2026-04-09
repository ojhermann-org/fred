from enum import StrEnum
from typing import Protocol

from request.interface.request import Request


class Builder(Protocol):
    def build(self) -> Request: ...
