from pydantic import BaseModel


def _to_str(v: object) -> str:
    if isinstance(v, bool):
        return str(v).lower()
    return str(v)


def for_request(bm: BaseModel) -> dict[str, str]:
    return {k: _to_str(v) for k, v in bm.model_dump().items() if v is not None}
