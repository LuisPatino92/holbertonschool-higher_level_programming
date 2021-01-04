#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    for i in range(list_length):
        try:
            new_list += [my_list_1[i] / my_list_2[i]]
        except ZeroDivisionError:
            print("division by 0")
            new_list += [0]
        except TypeError:
            print("wrong type")
            new_list += [0]
        except IndexError:
            print("wrong type")
            new_list += [0]

    return new_list