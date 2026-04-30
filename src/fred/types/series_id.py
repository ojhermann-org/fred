from typing import Annotated

from pydantic import Field

SeriesId = Annotated[str, Field(min_length=1)]
