# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - More Data Structures: Set, Dictionary

Continuing with data structures, this project is all about Sets and Dictionaries. Each file matches with one task of the project, some of them are basic excercises about manipulating data structures, the most are functions that needs to be called from other file.

---

## In this REPO:

>**0-square_matrix_simple.py**

Function that computes the square value of all integers of a matrix. Signature: `def square_matrix_simple(matrix=[]):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 0-main.py
    #!/usr/bin/python3
    square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

- `matrix` is spected to be a 2 dimensional array.
- The return is also a matix with exactly the same size as original, but with the squares.


>**1-search_replace.py**

Function that replaces all occurrences of an element by another in a new list. Signature: `def search_replace(my_list, search, replace):`. Here an instance of how this function can be used:

    #!/usr/bin/python3
    search_replace = __import__('1-search_replace').search_replace

    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)

- `my_list` is the initial list.
- `search` is the element to replace in the list.
- `replace` is the new element.

>**2-uniq_add.py**

Function that adds all unique integers in a list (only once for each integer). Signature: `def uniq_add(my_list=[]):`. Here an instance of how this function can be used:

    #!/usr/bin/python3
    uniq_add = __import__('2-uniq_add').uniq_add

    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

>**3-common_elements.py**

Function that returns a set of common elements in two sets. Signature: `def common_elements(set_1, set_2):`. Here an instance of how this function can be used:

    #!/usr/bin/python3
    common_elements = __import__('3-common_elements').common_elements

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

>**4-only_diff_elements.py**

Function that returns a set of all elements present in only one set. Signature: `def only_diff_elements(set_1, set_2):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 4-main.py
    #!/usr/bin/python3
    only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

    guillaume@ubuntu:~/0x04$ ./4-main.py
    ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']

>**5-number_keys.py**

Function that returns the number of keys in a dictionary.. Signature: `def number_keys(a_dictionary):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 5-main.py
    #!/usr/bin/python3
    number_keys = __import__('5-number_keys').number_keys

    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))

    guillaume@ubuntu:~/0x04$ ./5-main.py
    Number of keys: 3

>**6-print_sorted_dictionary.py**

Function that prints a dictionary by ordered keys.. Signature: `def print_sorted_dictionary(a_dictionary):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 6-main.py
    #!/usr/bin/python3
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)

    guillaume@ubuntu:~/0x04$ ./6-main.py
    Number: 89
    ids: [1, 2, 3]
    language: C
    track: Low level

>**7-update_dictionary.py**

Function that replaces or adds key/value in a dictionary.. Signature: `def update_dictionary(a_dictionary, key, value):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 7-main.py
    #!/usr/bin/python3
    update_dictionary = __import__('7-update_dictionary').update_dictionary
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    guillaume@ubuntu:~/0x04$ ./7-main.py
    language: Python
    number: 89
    track: Low level
    --
    language: Python
    number: 89
    track: Low level
    --
    --
    city: San Francisco
    language: Python
    number: 89
    track: Low level
    --
    city: San Francisco
    language: Python
    number: 89
    track: Low level

- `key` argument must be always a string.
- `value` argument can be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created

>**8-simple_delete.py**

Function that deletes a key in a dictionary. Signature: `def simple_delete(a_dictionary, key=""):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 8-main.py
    #!/usr/bin/python3
    simple_delete = __import__('8-simple_delete').simple_delete
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    guillaume@ubuntu:~/0x04$ ./8-main.py
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    --
    Number: 89
    ids: [1, 2, 3]
    language: C
    --
    Number: 89
    ids: [1, 2, 3]
    language: C

>**9-multiply_by_2.py**

Function that returns a new dictionary with all values multiplied by 2. Signature: `def multiply_by_2(a_dictionary):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 9-main.py
    #!/usr/bin/python3
    multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    guillaume@ubuntu:~/0x04$ ./9-main.py
    Alex: 8
    Bob: 14
    John: 12
    Mike: 14
    Molly: 16
    --
    Alex: 16
    Bob: 28
    John: 24
    Mike: 28
    Molly: 32

- All the values are supossed to be integers.
- The function returns a new dictionary.

>**10-best_score.py**

    Function that returns a key with the biggest integer value. Signature: `def best_score(a_dictionary):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 10-main.py
    #!/usr/bin/python3
    best_score = __import__('10-best_score').best_score

    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

    guillaume@ubuntu:~/0x04$ ./10-main.py
    Best score: Molly
    Best score: None

- All the values are supossed to be integers.
- If no score found, `None` is returned.
- All students are supossed to have a different score.

>**11-multiply_list_map.py**

Function that returns a list with all values multiplied by a number without using any loops. Signature: `def multiply_list_map(my_list=[], number=0):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 11-main.py
    #!/usr/bin/python3
    multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)

    guillaume@ubuntu:~/0x04$ ./11-main.py
    [4, 8, 12, 16, 24]
    [1, 2, 3, 4, 6]

- Returns a new list with same length as my_list, each value is multiplied by number.
- Initial list wont be modified.

>**12-roman_to_int.py**

Function that converts a Roman numeral to an integer. Signature: `def roman_to_int(roman_string):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 12-main.py
    #!/usr/bin/python3
    """ Roman to Integer test file
    """
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    guillaume@ubuntu:~/0x04$ ./12-main.py
    X = 10
    VII = 7
    IX = 9
    LXXXVII = 87
    DCCVII = 707

- The number should be between 1 and 3999.
- If the input is `None`, or not a string, return 0.

>**100-weight_average.py**

Function that returns the weighted average of all integers tuple (`<score>`, `<weight>`). Signature: `def weight_average(my_list=[]):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 100-main.py
    #!/usr/bin/python3
    weight_average = __import__('100-weight_average').weight_average

    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))

    guillaume@ubuntu:~/0x04$ ./100-main.py
    Average: 2.80

- Returns 0 if the list is empty.

>**101-square_matrix_map.py**

Function that computes the square value of all integers of a matrix using `map`. Signature: `def square_matrix_map(matrix=[]):`. Here an instance of how this function can be used:

    guillaume@ubuntu:~/0x04$ cat 101-main.py
    #!/usr/bin/python3
    square_matrix_map = \
        __import__('101-square_matrix_map').square_matrix_map

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)

    guillaume@ubuntu:~/0x04$ ./101-main.py
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

- The callenge was to do it in three lines, without using loops.

>**102-complex_delete.py**

F. Signature: `def square_matrix_simple(matrix=[]):`. Here an instance of how this function can be used:

>**103-python.c**

F. Signature: `def square_matrix_simple(matrix=[]):`. Here an instance of how this function can be used:
-

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
