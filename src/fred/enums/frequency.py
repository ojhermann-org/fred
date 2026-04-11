from enum import StrEnum


class Frequency(StrEnum):
    daily = "d"
    weekly = "w"
    biweekly = "bw"
    monthly = "m"
    quarterly = "q"
    semiannual = "sa"
    annual = "a"
    weekly_ending_friday = "wef"
    weekly_ending_thursday = "weth"
    weekly_ending_wednesday = "wew"
    weekly_ending_tuesday = "wetu"
    weekly_ending_monday = "wem"
    weekly_ending_sunday = "wesu"
    weekly_ending_saturday = "wesa"
    biweekly_ending_wednesday = "bwew"
    biweekly_ending_monday = "bwem"
