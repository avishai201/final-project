import pytest
from termcolor import colored


# Create a function that returns a sorted string with no duplicate characters
def no_duplicates(a_string):
    return ''.join(sorted(set(a_string.lower())))


# Create a function that returns the words in reverse order:
def reversed_words(a_string):
    x = ' '.join(list(reversed(a_string.split())))
    return x.split()


# Create a function that returns a list of 4 character strings:
def four_char_strings(a_string):
    s = 4
    str_return = ([a_string[i:i+s] for i in range(0, len(a_string), s)])
    return str_return


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', 'circ', 'us']


a_string = input('please enter a string: ')

print(colored('The original string: \n', 'yellow',), (a_string))

print(colored('String with no duplicate characters:\n', 'yellow'), (no_duplicates(a_string)))
print(colored('The words in reverse order:\n', 'yellow'), (reversed_words(a_string)))
print(colored('List of 4 character strings:\n', 'yellow'), (four_char_strings(a_string)))

'''
test_no_duplicates()
test_reversed_words()
test_four_char_strings()
'''