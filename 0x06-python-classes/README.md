# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - Classes and Objects

First approach to OOP, in this project all the tasks are aimed to develop a Square model, step by step. I used constructor methods, some private attributes, and other related features.

---

## In this REPO:

>**0-square.py**

Empty class that defines a `Square`. Here an instance of how this empy class behaves:

    LuchoPatiño@practice:~/0x06$ cat 0-main.py
    #!/usr/bin/python3
    Square = __import__('0-square').Square

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)

    LuchoPatiño@practice:~/0x06$ ./0-main.py
    <class '0-square.Square'>
    {}


>**1-square.py**

This one has the same class but with the following attributes:

- Private instance attribute: size
- Instantiation with size (no type/value verification)

Here, an instance of how `Square` behaves:

    LuchoPatiño@practice:~/0x06$ cat 1-main.py
    #!/usr/bin/python3
    Square = __import__('1-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

    LuchoPatiño@practice:~/0x06$ ./1-main.py
    <class '1-square.Square'>
    {'_Square__size': 3}
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'


>**2-square.py**

The same `Square` class with two additional things:

- Now, `Size` is optional, 0 by default.
- If negative or not integer values are passed as size, exceptions will be raised.

Here an instance of how the class could be used:

    LuchoPatiño@practice:~/0x06$ cat 2-main.py
    #!/usr/bin/python3
    Square = __import__('2-square').Square

    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)

    LuchoPatiño@practice:~/0x06$ ./2-main.py
    <class '2-square.Square'>
    {'_Square__size': 3}
    <class '2-square.Square'>
    {'_Square__size': 0}
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    size must be an integer
    size must be >= 0

>**3-square.py**

The same `Square` class with a new method:

- Public instance method: `def area(self)`: that returns the current square area.

Here, an instance of how the `Square` class behave:

    LuchoPatiño@practice:~/0x06$ cat 3-main.py
    #!/usr/bin/python3
    Square = __import__('3-square').Square

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

    LuchoPatiño@practice:~/0x06$ ./3-main.py
    Area: 9
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    Area: 25

>**4-square.py**

The same `Square` class, but with a setter for `size` instead of a constructor.

Here an instance of how the class behaves:

    LuchoPatiño@practice:~/0x06$ cat 4-main.py
    #!/usr/bin/python3
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

    LuchoPatiño@practice:~/0x06$ ./4-main.py
    Area: 7921 for size: 89
    Area: 9 for size: 3
    size must be an integer

>**5-square.py**

The same `Square` class, but with a `my_print()` method that prints the `Square`.

Here an instance of how the method behaves:

    #!/usr/bin/python3
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

    LuchoPatiño@practice:~/0x06$ ./5-main.py
    ###
    ###
    ###
    --
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    --

    --

>**6-square.py**

The same `Square` class, but with a new instance attribute `position`:

Here an instance of how `Square` behaves:

    #!/usr/bin/python3
    Square = __import__('6-square').Square

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

    LuchoPatiño@practice:~/0x06$ ./6-main.py | tr " " "_" | cat -e
    ###$
    ###$
    ###$
    --$
    $
    _###$
    _###$
    _###$
    --$
    ___###$
    ___###$
    ___###$
    --$

>**101-square.py**

The same `Square` class, but now print(`Square instance`) has the same behavior than `my_print()` method.

    LuchoPatiño@practice:~/0x06$ cat 101-main.py
    #!/usr/bin/python3
    Square = __import__('101-square').Square

    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

    LuchoPatiño@practice:~/0x06$ ./101-main.py | tr " " "_" | cat -e
    #####$
    #####$
    #####$
    #####$
    #####$
    --$
    $
    ____#####$
    ____#####$
    ____#####$
    ____#####$
    ____#####$

>**102-square.py**

The same `Square` class, but now its instances has the ability to be compared with `==`, `!=`, `>`, `>=`, `<` and `<=`.

The comparrison is carried out with the area of the instance. Here an example of how the object behaves now:

    LuchoPatiño@practice:~/0x06$ cat 102-main.py
    #!/usr/bin/python3
    Square = __import__('102-square').Square

    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

    LuchoPatiño@practice:~/0x06$ ./102-main.py
    Square 5 < Square 6
    Square 5 <= Square 6
    Square 5 != Square 6

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
