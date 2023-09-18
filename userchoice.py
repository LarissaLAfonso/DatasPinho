
def type_of_input():
    """
    Asks the user if they want to input the dates in a file, in the console or 
    if they want to quit.

    Returns
    -------
    The type of user input.
    
    

    """
    
    user_choice = input("What is the chosen type of input?\nIf file, type 'F',\n if console input type 'C',\n if you want to quite type 'Q'.")
    user_choice = user_choice.upper()
        
    try:
        if user_choice == "F" or user_choice == "Q" or user_choice == "C":
            return user_choice
        else:
            raise ValueError
    except:
        print("Your input is invalid. Please type one of the designated inputs.")
        type_of_input()

        

        
