from typing import Protocol


class Params(Protocol):
    def for_request(self) -> dict[str, str]: ...
