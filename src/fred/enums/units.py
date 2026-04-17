from enum import StrEnum


class Units(StrEnum):
    levels = "lin"
    change = "chg"
    change_from_one_year_ago = "ch1"
    percent_change = "pch"
    percent_change_from_one_year_ago = "pc1"
    compounded_annual_rate_of_change = "pca"
    continuously_compounded_rate_of_change = "cch"
    continuously_compounded_annual_rate_of_change = "cca"
    natural_log = "log"
