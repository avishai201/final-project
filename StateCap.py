import sys
import pytest
import ast
from pathlib import Path


def dic_file():
    dir_path = Path.cwd()/'capital_dic'  # current working directory
    file_path = dir_path  # path of dic file
    with open(file_path, "r") as data:  # read permission only
        dict = ast.literal_eval(data.read())
    return dict


# 1. Print the state capital of Idaho
def capital_of_Idaho():
    Idaho_capital = dic_file().get("Idaho", "")
    print(f"The capital city of Idaho is {Idaho_capital}\n")


# 2. Print all states.
def all_states():
    for states in dic_file().keys():
        print(states)


# 3. Print all capitals.
def all_capitals():
    for capitals in dic_file().values():
        print(capitals)


#4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
def states_capitals_string():
    x = ','.join(' --> '.join((key, val)) for (key, val) in dic_file().items())
    print(x)


# 5. Ensure the string you created in 4. is alphabetically sorted by state
def states_capitals_string_alphabetically():
    for i in sorted(dic_file().keys()):
        print(i, end=" ")


# Get State per a capital city
def get_state(capital):
    for key, value in dic_file().items():  #  key = state
        if capital == value:
            print(f"{capital} is the capital of {key}")


# Get capital city per state
def get_capital(state):
    for key, value in dic_file().items():
        if state == key:
            print(f"{value} is the capital of {state}")




### Test my code ###


def test_state_to_capital():
    assert 'Cheyenne' == dic_file()['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        dic_file()['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')



def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


def Results(Idaho_capital, states, capitas):
    print(Idaho_capital)
    print(states)
    print(capitas)


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())


