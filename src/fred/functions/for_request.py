from pydantic import BaseModel


def for_request(bm: BaseModel) -> dict[str, str]:
    return {k: str(v) for k, v in bm.model_dump().items() if v is not None}
