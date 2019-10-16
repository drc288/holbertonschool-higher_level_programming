#!/usr/bin/python3
"""
    MyList - Create object of list
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> print(my_list)
    [1]
"""
class MyList(list):
    """
        print_sorted - print the sorted list
    """
    def print_sorted(self):
        print(sorted(self))

