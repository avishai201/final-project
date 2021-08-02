from StateCap import *

user_menu = str("")

while user_menu != "0":
    user_menu = input("""Select option:
        1. Print the state capital of Idaho
        2. Print all states
        3. Print all capitals.
        4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
        5. Alphabetically sorted by state
        6. Enter a state and find the capital city
        7. Enter a capital and find the state
        0. Exit 
        
        Please enter your option:  """)

    if user_menu == "1":  # capital of Idaho
        capital_of_Idaho()

    if user_menu == "2":  # all states
        all_states()

    if user_menu == "3":  # all capitals
        all_capitals()

    if user_menu == "4":  # string of states and capitols
        states_capitals_string()

    if user_menu == "5":  # Alphabetically sorted string
        states_capitals_string_alphabetically()

    if user_menu == "6":
        capital = input("Enter the capital to find the state: ")
        get_state(capital)

    if user_menu == "7":
        state = input("Enter the state to find the capital: ")
        get_capital(state)



