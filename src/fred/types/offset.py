from typing import Annotated

from pydantic import Field

Offset = Annotated[int, Field(ge=0)]
