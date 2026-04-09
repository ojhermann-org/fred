from fred.request.enum.endpoint import Endpoint


class Request:
    def __init__(self, endpoint: Endpoint, parameters: dict[str, str]) -> None:
        self._endpoint: Endpoint = endpoint
        self._parameters: dict[str, str] = parameters

    def endpoint(self) -> Endpoint:
        return self._endpoint

    def parameters(self) -> dict[str, str]:
        return self._parameters
