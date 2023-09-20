import datecalculator
import userchoice

def calculatediff(dates):
    """
    Calculates the amount of days between two dates.

    Parameters
    ----------
    dates : string
        Inputed dates.

    Returns
    -------
    None.

    """
    try:
        date_1, date_2 = dates.split(" - ")
        date_1 = datecalculator.parse_date_string(date_1)
        date_2 = datecalculator.parse_date_string(date_2)
        print(datecalculator.calculate_days_between_dates(date_1, date_2))
    except Exception as error:
        print(f"There was an error while converting your dates:\n {error}")
        

user_input = userchoice.type_of_input()

if user_input == "Q":
    print("You quit.")
elif user_input == "C":
    dates = input("Input dates.")
    calculatediff(dates)
elif user_input == "F":
    file_name = input("Input file path.")
    try:
        with open(file_name, "r") as file:
            dates = file.read()
            calculatediff(dates)
    except FileNotFoundError:
        print("The file you inputed does not exist.")

