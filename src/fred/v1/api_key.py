from typing import Annotated

from pydantic import StringConstraints

API_KEY = Annotated[
    str,
    StringConstraints(
        pattern="^[a-z0-9]{32}$",
        strip_whitespace=True,
    ),
]
