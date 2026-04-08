from datetime import date

from pydantic import BaseModel, Field

from fred.v1.api_key import ApiKey
from fred.v1.file_type import FileType
from fred.v1.order_by import OrderBy
from fred.v1.realtime import Realtime
from fred.v1.sort_order import SortOrder


class Parameters(BaseModel):
    api_key: ApiKey = Field(...)
    # tests: raises when not passed (unit_test)

    file_type: FileType = Field(default=FileType.xml)
    # tests: uses xml when no parameter given (contract_test, unit_test); uses xml when xml is passed (unit_test); uses json when json is passed (unit_test); raises when something else is passed (unit_test)

    realtime_start: Realtime = Field(default=date.today().isoformat())
    # tests: uses today when nothing is passed (contract_test, unit_test)

    realtime_end: Realtime = Field(default=date.today().isoformat())
    # tests: uses today when nothing is passed (contract_test, unit_test)

    limit: int = Field(default=1000, gt=0, lt=1001)
    # tests: uses 1000 when nothing is passed (contract_test, unit_test); raises when a negative int is passed (unit_test); raises when a value greater than 1000 is passed (unit_test)

    offset: int = Field(default=0, gt=-1)
    # tests: uses 0 when nothing is passed (contract_test, unit_test); raises when a negative int is passed (unit_test)

    order_by: OrderBy = Field(default=OrderBy.source_id)
    # tests: uses source_id when nothing is passed (contract_test, unit_test); works when any OrderBy value is passed (contract_test, unit_test); raises when any other value is passed (contract_test, unit_test)

    sort_order: SortOrder = Field(default=SortOrder.asc)
    # tests: user asc when nothing is passed (contract_teset, unit_test); works when any SortOrder value is passed (contract_test, unit_test); raises when any other value is passed (contract_test, unit_test)
