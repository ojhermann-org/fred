from typing import Annotated

from pydantic import Field

ReleaseID = Annotated[int, Field(ge=1)]
