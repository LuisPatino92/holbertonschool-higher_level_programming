# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - More Classes and Objects

The second project on the OOP paradigm. Again the mandatory tasks are about modeling a simple object (a rectangle this time), and the goal chased is to understand deeply the @properties decorator, the public, private, and protected attributes and their differences.

---

## In this REPO:

>**[0-rectangle.py](0-rectangle.py)**

**Empty** class that defines a rectangle. Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 0-main.py
    #!/usr/bin/python3
    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)

    Lucho@Python_0x08$ ./0-main.py
    <class '0-rectangle.Rectangle'>
    {}


>**[1-rectangle.py](1-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

Here an instance of its conceivable usage:

    #!/usr/bin/python3
    Rectangle = __import__('1-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

    Lucho@Python_0x08$ ./1-main.py
    {'_Rectangle__height': 4, '_Rectangle__width': 2}
    {'_Rectangle__height': 3, '_Rectangle__width': 10}

>**[2-rectangle.py](2-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 2-main.py
    #!/usr/bin/python3
    Rectangle = __import__('2-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.    perimeter()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.    perimeter()))

    Lucho@Python_0x08$ ./2-main.py
    Area: 8 - Perimeter: 12
    --
    Area: 30 - Perimeter: 26

>**[3-rectangle.py](3-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 3-main.py
    #!/usr/bin/python3
    Rectangle = __import__('3-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.    perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))

    Lucho@Python_0x08$ ./3-main.py
    Area: 8 - Perimeter: 12
    ##
    ##
    ##
    ##
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    --
    ##########
    ##########
    ##########
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>

>**[4-rectangle.py](4-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 4-main.py
    #!/usr/bin/python3
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))

    Lucho@Python_0x08$ ./4-main.py
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7cc88
    --
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7ccc0
    --
    False
    True

>**[5-rectangle.py](5-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 5-main.py
    #!/usr/bin/python3
    Rectangle = __import__('5-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.    perimeter()))

    del my_rectangle

    try:
        print(my_rectangle)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    Lucho@Python_0x08$ ./5-main.py
    Area: 8 - Perimeter: 12
    Bye rectangle...
    [NameError] name 'my_rectangle' is not defined

>**[6-rectangle.py](6-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Public class attribute `number_of_instances`:

  - Initialized to 0.
  - Incremented during each new instance instantiation.
  - Decremented during each instance deletion.


Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 6-main.py
    #!/usr/bin/python3
    Rectangle = __import__('6-rectangle').Rectangle

    my_rectangle_1 = Rectangle(2, 4)
    my_rectangle_2 = Rectangle(2, 4)
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_1
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
    del my_rectangle_2
    print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

    Lucho@Python_0x08$ ./6-main.py
    2 instances of Rectangle
    Bye rectangle...
    1 instances of Rectangle
    Bye rectangle...
    0 instances of Rectangle

>**[7-rectangle.py](7-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Public class attribute `number_of_instances`:
  - Initialized to 0.
  - Incremented during each new instance instantiation.
  - Decremented during each instance deletion.
- Public class attribute `print_symbol`:
  - Initialized to #
  - Used as symbol for string representation
  - Can be any type

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 7-main.py
    #!/usr/bin/python3
    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    my_rectangle_3.print_symbol = ["C", "is", "fun!"]
    print(my_rectangle_3)

    print("--")

    Lucho@Python_0x08$ ./7-main.py
    ########
    ########
    ########
    ########
    --
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    &&&&&&&&
    --
    ##
    --
    CC
    --
    CCCCCCC
    CCCCCCC
    CCCCCCC
    --
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']    ['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
    --
    Bye rectangle...
    Bye rectangle...
    Bye rectangle...

>**[8-rectangle.py](8-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Public class attribute `number_of_instances`:
  - Initialized to 0.
  - Incremented during each new instance instantiation.
  - Decremented during each instance deletion.
- Public class attribute `print_symbol`:
  - Initialized to #
  - Used as symbol for string representation
  - Can be any type
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area.
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError`  - exception with the message `rect_1 must be an instance of Rectangle`.
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError`  - exception with the message `rect_2 must be an instance of Rectangle`.
  - Returns `rect_1` if both have the same area value.

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 8-main.py
    #!/usr/bin/python3
    Rectangle = __import__('8-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    Lucho@Python_0x08$ ./8-main.py
    my_rectangle_1 is bigger or equal to my_rectangle_2
    my_rectangle_2 is bigger than my_rectangle_1
    Bye rectangle...
    Bye rectangle...

>**[9-rectangle.py](9-rectangle.py)**

Class that defines a rectangle whit the following attributes and methods:

- Private instance attribute: `width`.
- Private instance attribute: `height`.
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area.
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter.
  - if `width` or `height` is equal to 0, `perimeter` has to be equal to 0.
- `print()` and `str()` should print the rectangle with the character `#`: (see example below).
  - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below).
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted.
- Public class attribute number_of_instances:
  - Initialized to 0.
  - Incremented during each new instance instantiation.
  - Decremented during each instance deletion.
- Public class attribute print_symbol:
  - Initialized to #
  - Used as symbol for string representation
  - Can be any type
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area.
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError`  - exception with the message `rect_1 must be an instance of Rectangle`.
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError`  - exception with the message `rect_2 must be an instance of Rectangle`.
  - Returns `rect_1` if both have the same area value.
- Class method `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`.

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ cat 9-main.py
    #!/usr/bin/python3
    Rectangle = __import__('9-rectangle').Rectangle

    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()    ))
    print(my_square)

    Lucho@Python_0x08$ ./9-main.py
    Area: 25 - Perimeter: 20
    #####
    #####
    #####
    #####
    #####
    Bye rectangle...

>**[101-nqueens.py](101-nqueens.py)**

Advanced task. Program that solves the N queens problem.

- Usage `nqueens N`
  - If wrong number of arguments passed, the program prints: `Usage: nqueens N`.
  - `N` must be at least 4.
  - The program print every possible solution. One solution per line.

Here an instance of its conceivable usage:

    Lucho@Python_0x08$ ./101-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
    Lucho@Python_0x08$ ./101-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

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
