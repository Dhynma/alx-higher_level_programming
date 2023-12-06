#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''
    A function that traverses through a list for an element that matches
    search and modifies it with replace, then returns a new list.
    @elem: Elements
    '''
    if not my_list:
        return my_list

    new_lst = [elem if elem != search else replace for elem in my_list]
    return new_lst
