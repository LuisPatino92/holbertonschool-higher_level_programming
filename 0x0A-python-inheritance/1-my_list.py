#!/usr/bin/python3
"""This module has a Class MyList derived from list"""


class MyList(list):
    """Class derived from list class with a new method to print sorted"""

    def print_sorted(self):
        """Method that prints the list in ascending order"""

        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
