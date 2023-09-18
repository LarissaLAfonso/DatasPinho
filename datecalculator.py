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
    year = int(year)
    month_number, month_days = months[month]

    if (month == "Fevereiro") and verify_leap_year(year):
        month_days = 29

    if day > month_days:
        raise ValueError(f"The month {month} doesn't have day {day}")

    return dt.datetime(year, month_number, day)

