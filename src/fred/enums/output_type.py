from enum import IntEnum


class OutputType(IntEnum):
    obs_by_real_time_period = 1
    obs_by_vintage_date_all = 2
    obs_by_vintage_date_new_and_revised = 3
    obs_initial_release = 4
