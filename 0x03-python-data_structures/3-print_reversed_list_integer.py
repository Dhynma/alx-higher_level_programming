#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    """Prints all integers of a list in reverse order."""
    if my_list is None:
        return

    reversed_list = list(reversed(my_list))
    for number in reversed_list:
        print('{:d}'.format(number))
