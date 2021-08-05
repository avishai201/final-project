import sys
import pytest
import ast
from pathlib import Path
from termcolor import colored


def dic_file():
    dir_path = Path.cwd()/'capital_dic'  # current working directory
    file_path = dir_path  # path of dic file
    with open(file_path, "r") as data:  # read permission only
        dict = ast.literal_eval(data.read())
    return dict


# 1. Print the state capital of Idaho #
def capital_of_Idaho():
    Idaho_capital = dic_file().get("Idaho", "")
    print(colored(f'The capital city of Idaho is {Idaho_capital}\n', 'yellow'))


# 2. Print all states.
def all_states():
    for states in dic_file().keys():
        print(colored(states, 'yellow'))


# 3. Print all capitals.
def all_capitals():
    for capitals in dic_file().values():
        print(colored(capitals, 'yellow'))


# 4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...' #
def states_capitals_string():
    str = ' , '.join(' --> '.join((key, val)) for (key, val) in dic_file().items())
    print(colored(str, 'yellow'))


# 5. Ensure the string you created in 4. is alphabetically sorted by state #
def states_capitals_string_alphabetically():
    for i in sorted(dic_file().keys()):
        print(colored(i, 'yellow'))


def get_state(capital):
    if capital == ' ':
        KeyError('param is not set')
    msg = 'Sorry your capital is not exist'
    state_list = []                              # If two states have the same capital name the are stored here #
    for state, value in dic_file().items():
        if capital == value:
            msg = state
            state_list.append(state)
    if msg == 'Sorry your capital is not exist':
        print(colored(msg, 'red'))
    elif len(state_list) > 1:
        print(colored('There is more than 1 option, the States are: ', 'yellow'), (str(state_list)))
        msg = ''.join(state_list)
    else:
        print(colored(f'{capital} is the capital of {msg}', 'yellow'))
    return msg


# Get capital city per state #
def get_capital(state):
    if state == ' ':
        KeyError('param is not set')
    msg = 'Sorry your state is not found'
    for key, capital in dic_file().items():
        if state == key:
            msg = capital
    if msg == 'Sorry your state is not found':
        print(colored(msg, 'red'))
    else:
        print(colored(f'{msg} is the capital of {state}', 'yellow'))
    return msg


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


