from typing import Annotated

from pydantic import Field

SourceId = Annotated[int, Field(ge=1)]
