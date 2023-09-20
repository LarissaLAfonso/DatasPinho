import datecalculator
import userchoice

while True:
    user_input = userchoice.type_of_input()
    
    if user_input == "Q":
        print("You quit.")
        break
    elif user_input == "C":
        dates = input("Input dates.")
        datecalculator.calculate_days_between_dates(dates)
    elif user_input == "F":
        file_name = input("Input file path.")
        try:
            with open(file_name, "r") as file:
                dates = file.read()
                datecalculator.calculate_days_between_dates(dates)
        except FileNotFoundError:
            print("The file {file_name} does not exist")
