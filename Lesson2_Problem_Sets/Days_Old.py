# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def validate_input(year1, month1, day1, year2, month2, day2):
    args = [year1, month1, day1, year2, month2, day2]
    i = 0
    while i < len(args):
        if args[i] <= 0 or type(args[1]) != int:
            print(f"Invalid input {args[i]}, must be positive integer.")
        i += 1

    if year2 < year1:
        print(f"Invalid input, current date must be equal or larger than birthday.")
    elif year2 == year1:
        if month2 < month1:
            print(f"Invalid input, current date must be equal or larger than birthday.")
        elif month2 == month1:
            if day2 < day1:
                print(f"Invalid input, current date must be equal or larger than birthday.")

    if day1 > check_days_per_month(year1, month1) or day2 > check_days_per_month(year2, month2):
        print("Incorrect input date!")

    return

def check_leap_year(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def check_days_per_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if check_leap_year(year):
            return 29
        return 28

def check_days_so_far(year, month, day):
    i = 1
    days = 0
    while i < month:
        days += check_days_per_month(year, i)
        i += 1
    days += day
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    validate_input(year1, month1, day1, year2, month2, day2)
    year = year1
    counter = 0
    while year < year2:
        if check_leap_year(year):
            counter += 1
        year += 1
    days_of_year_gap = 365*(year2-year1) + counter
    days_of_month_and_day_gap = check_days_so_far(year2, month2, day2) - check_days_so_far(year1, month1, day1)

    return days_of_year_gap + days_of_month_and_day_gap

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,30), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        assert daysBetweenDates(*args) == answer

test()
