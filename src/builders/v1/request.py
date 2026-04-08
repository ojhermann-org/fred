from pydantic import BaseModel, ConfigDict


class Request(BaseModel):
    model_config = ConfigDict(frozen=True)

    url: str
    params: dict[str, str]
