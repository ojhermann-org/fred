from enum import StrEnum


class SeasonalAdjustment(StrEnum):
    yes = "Seasonally Adjusted"
    no = "Not Seasonally Adjusted"
    saar = "Seasonally Adjusted Annual Rate"
