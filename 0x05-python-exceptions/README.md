# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - Exceptions

Some simple tasks intended for students to get a better understanding of what are exceptions and how to handle them.

---

## In this REPO:

>**0-safe_print_list.py**

Function that prints x elements of a list. Signature: `def safe_print_list(my_list=[], x=0):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 0-main.py
    #!/usr/bin/python3
    safe_print_list = __import__('0-safe_print_list').safe_print_list

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

    LuchoPatiño@practice$ ./0-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345
    nb_print: 5

- my_list can contain any type (integer, string, etc.)
- All elements will be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
- Returns the real number of elements printed

>**1-safe_print_integer.py**

Function that prints an integer with `"{:d}".format()"`. Signature: `def safe_print_integer(value):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 1-main.py
    #!/usr/bin/python3
    safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    LuchoPatiño@practice$ ./1-main.py
    89
    -89
    Holberton is not an integer

- value can be any type (integer, string, etc.)
- The integer will be printed followed by a new line
- Returns True if value has been correctly printed (it means the value is an- integer)
- Otherwise, returns False

>**2-safe_print_list_integers.py**

Function that prints the first x elements of a list and only integers. Signature: `def safe_print_list_integers(my_list=[], x=0):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 2-main.py
    #!/usr/bin/python3
    safe_print_list_integers = \
        __import__('2-safe_print_list_integers').safe_print_list_integers

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

    LuchoPatiño@practice$ ./2-main.py
    12
    nb_print: 2
    12345
    nb_print: 5
    12345Traceback (most recent call last):
      File "./2-main.py", line 14, in <module>
        nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
      File "/0x05/2-safe_print_list_integers.py", line 7, in     safe_print_list_integers
        print("{:d}".format(my_list[i]), end="")
    IndexError: list index out of range

- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other - type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception - will occur
- Returns the real number of integers printed

>**3-safe_print_division.py**

Function that divides 2 integers and prints the result. Signature: `def safe_print_division(a, b):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 3-main.py
    #!/usr/bin/python3
    safe_print_division = __import__('3-safe_print_division').

    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result)

    LuchoPatiño@practice$ ./3-main.py
    Inside result: 6.0
    12 / 2 = 6.0
    Inside result: None
    12 / 0 = None

- a and b are supposed to be integers.
- The result of the division should print on the finally: section preceded by
- Inside result:
- Returns the value of the division, otherwise: None

>**4-list_division.py**

Function that divides element by element 2 lists. Signature: `def list_division(my_list_1, my_list_2, list_length):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 4-main.py
    #!/usr/bin/python3
    list_division = __import__('4-list_division').list_division

    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    LuchoPatiño@practice$ ./4-main.py
    [5.0, 2.0, 1.0]
    --
    division by 0
    wrong type
    out of range
    [5.0, 0, 0, 2.0, 0]

- my_list_1 and my_list_2 can contain any type (integer, string, etc.)
- list_length can be bigger than the length of both lists
- Returns a new list (length = list_length) with all divisions
- If 2 elements can’t be divided, the division result should be equal to 0
- If an element is not an integer or float:
- print: wrong type

- If the division can’t be done (/0):

  - print: division by 0

- If my_list_1 or my_list_2 is too short

  - print: out of range

>**5-raise_exception.py**

Function that raises a type exception. Signature: `def raise_exception():` Here an instance of how this function can be used:

    #!/usr/bin/python3
    raise_exception = __import__('5-raise_exception').raise_exception

    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")

    LuchoPatiño@practice$ ./5-main.py
    Exception raised

>**6-raise_exception_msg.py**

Function that raises a name exception with a message. Signature: `def raise_exception_msg(message=""):` Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 6-main.py
    #!/usr/bin/python3
    raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)

    LuchoPatiño@practice$ ./6-main.py
    C is fun

>**100-safe_print_integer_err.py**

Function that prints an integer in safe mode. Signature: `def safe_print_integer_err(value):`. Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 100-main.py
    #!/usr/bin/python3
    safe_print_integer_err = \
        __import__('100-safe_print_integer_err').safe_print_integer_err

    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    LuchoPatiño@practice$ ./100-main.py
    89
    -89
    Exception: Unknown format code 'd' for object of type 'str'
    Holberton is not an integer
    LuchoPatiño@practice$ ./100-main.py 2> /dev/null
    89
    -89
    Holberton is not an integer

- value can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns True if value has been correctly printed (it means the value is an integer)
- Otherwise, returns False and prints in stderr the error precede by Exception:

>**101-safe_function.py**

Function that executes a function safely. Signature: `def safe_function(fct, *args):`. Here an instance of how this function can be used:

    LuchoPatiño@practice$ cat 101-main.py
    #!/usr/bin/python3
    safe_function = __import__('101-safe_function').safe_function


    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))

    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))


    def print_list(my_list, len):
        i = 0
        while i < len:
            print(my_list[i])
            i += 1
        return len

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))

    LuchoPatiño@practice$ ./101-main.py
    result of my_div: 5.0
    Exception: division by zero
    result of my_div: None
    1
    2
    3
    4
    Exception: list index out of range
    result of print_list: None
    LuchoPatiño@practice$ ./101-main.py 2> /dev/null
    result of my_div: 5.0
    result of my_div: None
    1
    2
    3
    4
result of print_list: None

- `fct` must be always a pointer to a function
- Returns the result of the function,
- Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:

---

### Author

All the code in this REPO was made by **Luis Patiño** in 2020/2021, as part of Holberton School developer training.

---

<div>
<div align="center">
<img display="block" alt="Holberton Logo" width="50%" src="https://www.holbertonschool.com/holberton-logo.png">
</div>
<p align="center"><b>2020 - 2021</b></p>
</div>

---
