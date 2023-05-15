"""Function for return if year is a leap or not"""

def leap_year(year):
    """Return if year is a leap or not

    Args:
        year (integer): Year

    Returns:
        Boolean: True for leap year or False for not leap year
    """
    return True if (year % 4 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False

print(leap_year(2100))