def is_leap_year(year: int) -> bool:
    """Checks if a given year is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    