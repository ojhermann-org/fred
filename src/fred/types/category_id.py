from typing import Annotated

from pydantic import Field

CategoryID = Annotated[int, Field(ge=0)]
