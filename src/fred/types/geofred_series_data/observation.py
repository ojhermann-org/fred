from pydantic import BaseModel


class Observation(BaseModel):
    region: str
    code: str
    value: float
    series_id: str
