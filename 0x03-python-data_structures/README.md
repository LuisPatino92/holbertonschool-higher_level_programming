# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - Data Structures: Lists, Tuples

Project aimed to learn about Lists and Tuples in python, its use, its aplications and its more common methods.

---

## In this REPO:

>**0-print_list_integer.py**

Function that prints all integer in a list. Its signature is `def print_list_integer(my_list=[]):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 0-main.py
    #!/usr/bin/python3
    print_list_integer = __import__('0-print_list_integer').    print_list_integer

    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)

    guillaume@ubuntu:~/0x03$ ./0-main.py
    1
    2
    3
    4
    5

>**1-element_at.py**

Function that retrieves an element from a list. Its signature is `def element_at(my_list, idx):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 1-main.py
    #!/usr/bin/python3
    element_at = __import__('1-element_at').element_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)    ))

    guillaume@ubuntu:~/0x03$ ./1-main.py
    Element at index 3 is 4

Wheter the input `idx` is negative or out of range the return value will be `None`.

>**2-replace_in_list.py**

Function that replaces an element of a list at a specific position. Its signature is `def replace_in_list(my_list, idx, element):`. Here an exaple of the usage and the expected output:

guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

    guillaume@ubuntu:~/0x03$ ./2-main.py
    [1, 2, 3, 9, 5]
    [1, 2, 3, 9, 5]

If idx is negative, the function wont modify anything, and will return the original list. If idx is out of range (> of number of element in `my_list`), the function wont modify anything, and will return the original list.

>**3-print_reversed_list_integer.py**

Function that print all elements of a list in reverse. Its signature is `def print_reversed_list_integer(my_list=[]):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 3-main.py
    #!/usr/bin/python3
    print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)

    guillaume@ubuntu:~/0x03$ ./3-main.py
    5
    4
    3
    2
    1

>**4-new_in_list.py**

Function that replaces an element in a list at a specific position without modifying the original list. Its signature is `def new_in_list(my_list, idx, element):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 4-main.py
    #!/usr/bin/python3
    new_in_list = __import__('4-new_in_list').new_in_list

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

    guillaume@ubuntu:~/0x03$ ./4-main.py
    [1, 2, 3, 9, 5]
    [1, 2, 3, 4, 5]

If `idx` is negative, the function will return a copy of the original `list`. If idx is out of range (> of number of element in `my_list`), the function will return a copy of the original `list`.

>**5-no_c.py**

Function that removes all characters c and C from a string. Its signature is `def no_c(my_string):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 5-main.py
    #!/usr/bin/env python3
    no_c = __import__('5-no_c').no_c

    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))

    guillaume@ubuntu:~/0x03$ ./5-main.py
    Holberton Shool
    hiago
     is fun!

The function returns the new string.

>**6-print_matrix_integer.py**

Function that prints a matrix of integers. Its signature is `def print_matrix_integer(matrix=[[]]):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 6-main.py
    #!/usr/bin/python3
    print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

    guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
    1 2 3$
    4 5 6$
    7 8 9$
    --$

The matrix is spected to contain only integers.

>**7-add_tuple.py**

Function that adds two tuples. Its signature is `def add_tuple(tuple_a=(), tuple_b=()):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 7-main.py
    #!/usr/bin/python3
    add_tuple = __import__('7-add_tuple').add_tuple

    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))

    guillaume@ubuntu:~/0x03$ ./7-main.py
    (89, 100)
    (2, 89)
    (1, 89)

- The first element is the addition of the first element of each argument.
- The second element is the addition of the second element of each argument.
- If a tuple is smaller than 2, the value 0 is used for each missing integer.
- If a tuple is bigger than 2, only the first 2 integers are used.

>**8-multiple_returns.py**

Function that returns a tuple with the length of a string and its first character. Its signature is `def multiple_returns(sentence):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 8-main.py
    #!/usr/bin/python3
    multiple_returns = __import__('8-multiple_returns').multiple_returns

    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))

    guillaume@ubuntu:~/0x03$ ./8-main.py
    Length: 32 - First character: A

- If the sentence is empty, the first character will be equal to `None`.

>**9-max_integer.py**

Function that finds the biggest integer of a list. Its signature is `def max_integer(my_list=[]):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 9-main.py
    #!/usr/bin/python3
    max_integer = __import__('9-max_integer').max_integer

    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))

    guillaume@ubuntu:~/0x03$ ./9-main.py
    Max: 90

- If the list is Empty `None` is returned.
- The list must only contain numbers.

>**10-divisible_by_2.py**

Function that finds all multiples of 2 in a list. Its signature is `def divisible_by_2(my_list=[]):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 10-main.py
    #!/usr/bin/python3
    divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

    guillaume@ubuntu:~/0x03$ ./10-main.py
    0 is divisible by 2
    1 is not divisible by 2
    2 is divisible by 2
    3 is not divisible by 2
    4 is divisible by 2
    5 is not divisible by 2
    6 is divisible by 2

- The return format is a new list with `True` or `False` values.

>**11-delete_at.py**

Function that deletes the item at a specific position in a list. Its signature is `def delete_at(my_list=[], idx=0):`. Here an exaple of the usage and the expected output:

    guillaume@ubuntu:~/0x03$ cat 11-main.py
    #!/usr/bin/python3
    delete_at = __import__('11-delete_at').delete_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)

    guillaume@ubuntu:~/0x03$ ./11-main.py
    [1, 2, 3, 5]
    [1, 2, 3, 5]

- If `idx` is negative or out of range nothing change, the same list is returned.

>**12-switch.py**

Given the original code, as it is shown here:

    #!/usr/bin/python3
    a = 89
    b = 10
    # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
    print("a={:d} - b={:d}".format(a, b))

The activity is to add code in line 4, where it says: `# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE` in order to switck a and b values. It must be done in just one line.

>**13-is_palindrome.c**

Function that checks if a singly linked list is a palindrome. The function is written in C, its signature is: `int is_palindrome(listint_t **head)`. Here is the structure of a singly linked list node:

    /**
     * struct listint_s - singly linked list
     * @n: integer
     * @next: points to the next node
     *
     * Description: singly linked list node structure
     * for Holberton project
     */
    typedef struct listint_s
    {
        int n;
        struct listint_s *next;
    } listint_t;

- The function returns 0 if it's not a palindrome, 1 if it is.
- An empty list is considered a palindrome.


>**lists.h**

Header file for the `is_palindrome()` function.

>**100-print_python_list_info.c**

HERE

---

### Author

All the code in this REPO was made by **Luis Patiño** in 2020, as part of Holberton School developer training.

---

<div>
<div align="center">
<img display="block" alt="Holberton Logo" width="50%" src="https://www.holbertonschool.com/holberton-logo.png">
</div>
<p align="center"><b>2020</b></p>
</div>

---
