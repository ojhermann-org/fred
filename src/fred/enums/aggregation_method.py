from enum import StrEnum


class AggregationMethod(StrEnum):
    average = "avg"
    sum = "sum"
    end_of_period = "eop"
