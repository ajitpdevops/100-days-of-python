def is_leap_year(year):
    """Checks if the given year is a leap year"""
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    else:
        return False

def days_in_month(year, month):
    """Takes Year and Month as input and returns the days in given month"""
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = month - 1
    
    if is_leap_year(year):
        month_days[1] = 29

    return month_days[i]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

days = days_in_month(year=year, month=month)
print(days)