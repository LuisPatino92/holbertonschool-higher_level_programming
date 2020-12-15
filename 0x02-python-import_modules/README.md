# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - import & modules

This project is aimed to teach how to import functions from another file, how to use imported functions, how to create a module, use dir(), prevent code in a script to be executed when imported, and use command-line arguments passed to python programs..

---

## In this REPO:

>**0-add.py**

 program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3, with some conditions

>**1-calculation.py**

Program that imports functions from the file calculator_1.py, does some Maths, and prints the result

>**2-args.py**

Program that prints the number of and the list of its arguments.

>**3-infinite_add.py**

Program that prints the result of the addition of all arguments.

>**4-hidden_discovery.py**

Program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

>**5-variable_load.py**

Program that imports the variable a from the file variable_load_5.py and prints its value.

>**100-my_calculator.py**

Program that imports all functions from the file calculator_1.py and handles basic operations.

>**101-easy_print.py**

Program that prints #pythoniscool, followed by a new line, in the standard output.

>**102-magic_calculation.py**

Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

    3           0 LOAD_CONST               1 (0)
                3 LOAD_CONST               2 (('add', 'sub'))
                6 IMPORT_NAME              0 (magic_calculation_102)
                9 IMPORT_FROM              1 (add)
               12 STORE_FAST               2 (add)
               15 IMPORT_FROM              2 (sub)
               18 STORE_FAST               3 (sub)
               21 POP_TOP

    4          22 LOAD_FAST                0 (a)
               25 LOAD_FAST                1 (b)
               28 COMPARE_OP               0 (<)
               31 POP_JUMP_IF_FALSE       94

    5          34 LOAD_FAST                2 (add)
               37 LOAD_FAST                0 (a)
               40 LOAD_FAST                1 (b)
               43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               46 STORE_FAST               4 (c)

    6          49 SETUP_LOOP              38 (to 90)
               52 LOAD_GLOBAL              3 (range)
               55 LOAD_CONST               3 (4)
               58 LOAD_CONST               4 (6)
               61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               64 GET_ITER
          >>   65 FOR_ITER                21 (to 89)
               68 STORE_FAST               5 (i)

    7          71 LOAD_FAST                2 (add)
               74 LOAD_FAST                4 (c)
               77 LOAD_FAST                5 (i)
               80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               83 STORE_FAST               4 (c)
               86 JUMP_ABSOLUTE           65
          >>   89 POP_BLOCK

    8     >>   90 LOAD_FAST                4 (c)
               93 RETURN_VALUE

    10    >>   94 LOAD_FAST                3 (sub)
               97 LOAD_FAST                0 (a)
              100 LOAD_FAST                1 (b)
              103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              106 RETURN_VALUE
              107 LOAD_CONST               0 (None)
              110 RETURN_VALUE

>**103-fast_alphabet.py**

Program that prints the alphabet in uppercase, followed by a new line.

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