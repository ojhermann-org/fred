from typing import Annotated

from pydantic import StringConstraints

ALPHA_NUMERIC_LOWERCASE_32_CHARS = "^[a-z0-9]{32}$"

ApiKey = Annotated[
    str,
    StringConstraints(
        pattern=ALPHA_NUMERIC_LOWERCASE_32_CHARS,
        strip_whitespace=True,
    ),
]
