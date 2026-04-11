from typing import Annotated

from pydantic import Field

Limit = Annotated[int, Field(ge=1, le=1000)]
