# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def validate_input(year1, month1, day1, year2, month2, day2):
    """
    To validate if all the inputs are positive integer assuming that
    you were not born in the same year as Jesus Christ or priori,
    also checking if you are a time traveller.
    """
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
    """
    Check if a year is a leap year
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

def check_days_per_month(year, month):
    """
    Given a year and moth, check if how many days are in
    that month
    """
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if check_leap_year(year):
            return 29
        return 28

def check_days_so_far(year, month, day):
    """
    Given a year and month and day, check how many days
    since the beginning of that year
    """
    i = 1
    days = 0
    while i < month:
        days += check_days_per_month(year, i)
        i += 1
    days += day
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    check the year differences and multiply by 365 and compensate with the number
    of leap years between them, then check the month and day data of each input
    to get the return of how many days from the beignning of that year in total
    for that input and minus those two numbers to get the difference.
    """
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
    """
    Noticing Pycharm will force you install pytest when you
    have a method called test(), thus using the default assert()
    method for testing
    """
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        assert daysBetweenDates(*args) == answer

test()
