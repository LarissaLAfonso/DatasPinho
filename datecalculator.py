import datetime as dt

def verify_leap_year(year):
    """
    Verify if the inputed year is a leap year.

    Parameters
    ----------
    year : int
        Input year.

    Returns
    -------
    bool
        TRUE if leap year, FALSE if not.

    >>> verify_leap_year(2004)
    True

    >>> verify_leap_year(1765)
    False

    >>> verify_leap_year(2000)
    True

    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

def parse_date_string(input_string):
    """
    Takes the inputed string and transforms it in a datetime.datetime object.

    Parameters
    ----------
    input_string : string
        Inputed date.

    Raises
    ------
    ValueError
        If the inputed number of days in a month is greater than the number of
        days that month has.

    Returns
    -------
    datetime.datetime
        The inputed day, in datetime form.

    >>> parse_date_string("18 de Setembro de 2022")
    datetime.datetime(2022, 9, 18, 0, 0)

    >>> parse_date_string("19 de Janeiro de 2010")
    datetime.datetime(2010, 1, 19, 0, 0)
    """
    months = {"Janeiro": (1, 31),
             "Fevereiro": (2, 28),
             "Março": (3, 31),
             "Abril": (4, 30),
             "Maio": (5, 31),
             "Junho": (6, 30),
             "Julho": (7, 31),
             "Agosto": (8, 31),
             "Setembro": (9, 30),
             "Outubro": (10, 31),
             "Novembro": (11, 30),
             "Dezembro": (12, 31)
             }

    day, month, year = input_string.split(" de ")
    day = int(day)
    month = month.title()
    year = int(year)
    try:
        month_number, month_days = months[month]
    except KeyError:
        raise ValueError(f"{month} isn't a valid month.")

    if (month == "Fevereiro") and verify_leap_year(year):
        month_days = 29

    if day > month_days or day < 1:
        raise ValueError(f"The month {month} doesn't have day {day}")

    return dt.datetime(year, month_number, day)

def calculate_days_between_dates(dates):
    """
    Calculates the amount of days between two dates.

    Parameters
    ----------
    dates : string
        Inputed dates.

    Returns
    -------
    None.

    >>> calculate_days_between_dates("25 de Janeiro de 69 - 25 de Fevereiro de 49")
    7274
    """
    try:
        date_1, date_2 = dates.split(" - ")
        date_1 = parse_date_string(date_1)
        date_2 = parse_date_string(date_2)
        timedelta = date_2 - date_1
        print(abs(timedelta.days))
    except Exception as error:
        print(f"There was an error while converting your dates:\n {error}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
