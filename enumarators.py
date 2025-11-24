from enum import Enum


class Weekday(Enum):
    SATURDAY = 1
    SUNDAY = 2
    MONDAY = 3
    TUESDAY = 4
    WEDNESDAY = 5
    THURSDAY = 6
    FRIDAY = 7


workday = Weekday.MONDAY
print(workday.name)
print(workday.value)
