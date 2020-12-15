#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copy_list = my_list[:]
    copy_list.reverse()
    for element in copy_list:
        print("{:d}".format(element))
    if len(my_list) == 0:
        print("")
