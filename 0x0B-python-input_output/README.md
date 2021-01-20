# Holberton School Project

>This repo is part of the Holberton School curriculum.

## Python - Input/Output

This project guides the Software Developer through the learning of how manage files with Python in order to automatize some tasks.

---

## In this REPO:

>**[0-read_file.py](0-read_file.py)**

Function that reads a text file and prints its content to stdout. Signature: `def read_file(filename=""):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 0-main.py
    #!/usr/bin/python3
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")

    Lucho@Hbtn_Project$ cat my_file_0.txt
    Holberton School offers a truly innovative approach to education:
    focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your     peers.

    A school every software engineer would have dreamt of!
    Lucho@Hbtn_Project$ ./0-main.py
    Holberton School offers a truly innovative approach to education:
    focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your     peers.

    A school every software engineer would have dreamt of!

>**[1-write_file.py](1-write_file.py)**

Function that writes a string in a file and returns the number of characters written. Signature: `def write_file(filename="", text=""):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 1-main.py
    #!/usr/bin/python3
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
    print(nb_characters)

    Lucho@Hbtn_Project$ ./1-main.py
    29
    Lucho@Hbtn_Project$ cat my_first_file.txt
    Holberton School is so cool!

>**[2-append_write.py](2-append_write.py)**

Function that appends a string at the end of the file and return the amount of chars written. Signature: `def append_write(filename="", text=""):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 2-main.py
    #!/usr/bin/python3
    append_write = __import__('2-append_write').append_write

    nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
    print(nb_characters_added)

    Lucho@Hbtn_Project$ cat file_append.txt
    cat: file_append.txt: No such file or directory
    Lucho@Hbtn_Project$ ./2-main.py
    29
    Lucho@Hbtn_Project$ cat file_append.txt
    Holberton School is so cool!
    Lucho@Hbtn_Project$ ./2-main.py
    29
    Lucho@Hbtn_Project$ cat file_append.txt
    Holberton School is so cool!
    Holberton School is so cool!

>**[3-to_json_string.py](3-to_json_string.py)**

Function returns the `JSON` representation of an string object. Signature: `def to_json_string(my_obj):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 3-main.py
    #!/usr/bin/python3
    to_json_string = __import__('3-to_json_string').to_json_string

    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

    my_dict = {
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)
    print(s_my_dict)
    print(type(s_my_dict))

    try:
        my_set = { 132, 3 }
        s_my_set = to_json_string(my_set)
        print(s_my_set)
        print(type(s_my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    Lucho@Hbtn_Project$ ./3-main.py
    [1, 2, 3]
    <class 'str'>
    {"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco",     "Tokyo"]}
    <class 'str'>
    [TypeError] {3, 132} is not JSON serializable

>**[4-from_json_string.py](4-from_json_string.py)**

Function that returns an object (Python datastructure) from a `JSON` string. Signature: `def from_json_string(my_str):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 4-main.py
    #!/usr/bin/python3
    from_json_string = __import__('4-from_json_string').from_json_string

    s_my_list = "[1, 2, 3]"
    my_list = from_json_string(s_my_list)
    print(my_list)
    print(type(my_list))

    s_my_dict = """
    {"is_active": true, "info": {"age": 36, "average": 3.14}, 
    "id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))

    try:
        s_my_dict = """
        {"is_active": true, 12 }
        """
        my_dict = from_json_string(s_my_dict)
        print(my_dict)
        print(type(my_dict))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    Lucho@Hbtn_Project$ ./4-main.py
    [1, 2, 3]
    <class 'list'>
    {'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco',     'Tokyo']}
    <class 'dict'>
    [ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)

>**[5-save_to_json_file.py](5-save_to_json_file.py)**

Function that writes an Object to a text file, using a `JSON` representation: . Signature: `def save_to_json_file(my_obj, filename):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 5-main.py
    #!/usr/bin/python3
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = { 132, 3 }
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    Lucho@Hbtn_Project$ ./5-main.py
    [TypeError] {3, 132} is not JSON serializable
    Lucho@Hbtn_Project$ cat my_list.json ; echo ""
    [1, 2, 3]
    Lucho@Hbtn_Project$ cat my_dict.json ; echo ""
    {"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active":     true}
    Lucho@Hbtn_Project$ cat my_set.json ; echo ""

>**[6-load_from_json_file.py](6-load_from_json_file.py)**

Function that creates an Object from a “JSON file”:. Signature: `def load_from_json_file(filename):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat my_fake.json
    {"is_active": true, 12 }
    Lucho@Hbtn_Project$ cat 6-main.py
    #!/usr/bin/python3
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    Lucho@Hbtn_Project$ cat my_list.json ; echo ""
    [1, 2, 3]
    Lucho@Hbtn_Project$ cat my_dict.json ; echo ""
    {"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active":     true}
    Lucho@Hbtn_Project$ cat my_fake.json ; echo ""
    {"is_active": true, 12 }
    Lucho@Hbtn_Project$ ./6-main.py
    [1, 2, 3]
    <class 'list'>
    {'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active':     True}
    <class 'dict'>
    [FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
    [ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)

>**[7-add_item.py](7-add_item.py)**

Script that adds all arguments to a Python list, and then save them to a file. Here an instance of how the script works:

    Lucho@Hbtn_Project$ cat add_item.json
    cat: add_item.json: No such file or directory
    Lucho@Hbtn_Project$ ./7-add_item.py
    Lucho@Hbtn_Project$ cat add_item.json ; echo ""
    []
    Lucho@Hbtn_Project$ ./7-add_item.py Holberton School
    Lucho@Hbtn_Project$ cat add_item.json ; echo ""
    ["Holberton", "School"]
    Lucho@Hbtn_Project$ ./7-add_item.py 89 Python C
    Lucho@Hbtn_Project$ cat add_item.json ; echo ""
    ["Holberton", "School", "89", "Python", "C"]

>**[8-class_to_json.py](8-class_to_json.py)**

Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object. Signature: ``. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 8-my_class.py
    #!/usr/bin/python3
    """ My class module
    """

    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    Lucho@Hbtn_Project$ cat 8-main.py
    #!/usr/bin/python3
    MyClass = __import__('8-my_class').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    Lucho@Hbtn_Project$ ./8-main.py
    <class '8-my_class.MyClass'>
    [MyClass] John - 89
    <class 'dict'>
    {'name': 'John', 'number': 89}
    Lucho@Hbtn_Project$
    Lucho@Hbtn_Project$ cat 8-my_class_2.py
    #!/usr/bin/python3
    """ My class module
    """

    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number = 4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

    Lucho@Hbtn_Project$ cat 8-main_2.py
    #!/usr/bin/python3
    MyClass = __import__('8-my_class_2').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

    Lucho@Hbtn_Project$ ./8-main_2.py
    <class '8-my_class_2.MyClass'>
    [MyClass] John - 4 => 1
    <class 'dict'>
    {'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}

>**[9-student.py](9-student.py)**

Definition of `Student` class, defining a student with `first_name`, `last_name`, `age`.

Here an instance of how an instance of the class is created and how behaves:

    Lucho@Hbtn_Project$ cat 9-main.py
    #!/usr/bin/python3
    Student = __import__('9-student').Student

    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))

    Lucho@Hbtn_Project$ ./9-main.py
    <class 'dict'>
    John
    <class 'str'>
    23
    <class 'int'>
    <class 'dict'>
    Bob
    <class 'str'>
    27
    <class 'int'>

>**[10-student.py](10-student.py)**

Definition of `Student` class, defining a student with `first_name`, `last_name`, `age`. Aditionally in this file is the definition of public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `10-class_to_json.py`):

Here an instance of how the class objects behaves:

    Lucho@Hbtn_Project$ cat 10-main.py
    #!/usr/bin/python3
    Student = __import__('10-student').Student

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)

    Lucho@Hbtn_Project$ ./10-main.py
    {'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
    {'age': 27, 'first_name': 'Bob'}
    {'age': 27}

>**[11-student.py](11-student.py)**

Definition of `Student` class, defining a student with `first_name`, `last_name`, `age`. Includes the definition of public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `10-class_to_json.py`):

Aditionally here is the public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance:

Here an instance of how the class objects behaves:

    Lucho@Hbtn_Project$ cat 11-main.py
    #!/usr/bin/python3
    import os
    import sys

    Student = __import__('11-student').Student
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")


    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

    Lucho@Hbtn_Project$ ./11-main.py student.json
    Initial student:
    <11-student.Student object at 0x7f832826eda0>
    <class '11-student.Student'>
    <class 'dict'>
    John Doe 23
    {"last_name": "Doe", "first_name": "John", "age": 23}
    Saved to disk
    Fake student:
    <11-student.Student object at 0x7f832826edd8>
    <class '11-student.Student'>
    Fake Fake 89
    Load dictionary from file:
    <11-student.Student object at 0x7f832826edd8>
    <class '11-student.Student'>
    John Doe 23
    Lucho@Hbtn_Project$ cat student.json ; echo ""
    {"last_name": "Doe", "first_name": "John", "age": 23}

>**[12-pascal_triangle.py](12-pascal_triangle.py)**

Function that returns a list of lists of integers representing the Pascal’s triangle of `n`. Signature: `def pascal_triangle(n):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 12-main.py
    #!/usr/bin/python3
    """
    12-main
    """
    pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))


    if __name__ == "__main__":
        print_triangle(pascal_triangle(5))

    Lucho@Hbtn_Project$
    Lucho@Hbtn_Project$ ./12-main.py
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]


>**[100-append_after.py](100-append_after.py)**

Function that inserts a line of text to a file, after each line containing a specific string. Signature: `def append_after(filename="", search_string="", new_string=""):`. Here an instance of how the function could be used:

    Lucho@Hbtn_Project$ cat 100-main.py
    #!/usr/bin/python3
    append_after = __import__('100-append_after').append_after

    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

    Lucho@Hbtn_Project$ cat append_after_100.txt
    At Holberton School,
    Python is really important,
    But it can be very hard if:
    - You don't get all Pythonic tricks
    - You don't have strong C knowledge.
    Lucho@Hbtn_Project$ ./100-main.py
    Lucho@Hbtn_Project$ cat append_after_100.txt
    At Holberton School,
    Python is really important,
    "C is fun!"
    But it can be very hard if:
    - You don't get all Pythonic tricks
    "C is fun!"
    - You don't have strong C knowledge.
    Lucho@Hbtn_Project$ ./100-main.py
    Lucho@Hbtn_Project$ cat append_after_100.txt
    At Holberton School,
    Python is really important,
    "C is fun!"
    "C is fun!"
    But it can be very hard if:
    - You don't get all Pythonic tricks
    "C is fun!"
    "C is fun!"
    - You don't have strong C knowledge.

>**[101-stats.py](101-stats.py)**

Scripts that reads from `stdin` line by line and computes metrics.

Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

Each 10 lines and after a keyboard interruption (CTRL + C), those statistics are printed (since the beginning):

- Total file size: File size: `<total size>`.
- where is the sum of all previous (see input format above).
- Number of lines by status code:

  - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`.
  - if a status code doesn’t appear, don’t print anything for this status code.
  - format: `<status code>: <number>`.
  - status codes should be printed in ascending order.

Here an instance of how the script operates:

    Lucho@Hbtn_Project$ cat 101-generator.py
    #!/usr/bin/python3
    import random
    import sys
    from time import sleep
    import datetime

    for i in range(10000):
        sleep(random.random())
        sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        ))
        sys.stdout.flush()

    Lucho@Hbtn_Project$ ./101-generator.py | ./101-stats.py
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
    File size: 11320
    200: 3
    301: 2
    400: 1
    401: 2
    403: 3
    404: 4
    405: 2
    500: 3
    File size: 16305
    200: 3
    301: 3
    400: 4
    401: 2
    403: 5
    404: 5
    405: 4
    500: 4
    ^CFile size: 17146
    200: 4
    301: 3
    400: 4
    401: 2
    403: 6
    404: 6
    405: 4
    500: 4
    Traceback (most recent call last):
      File "./101-stats.py", line 15, in <module>
    Traceback (most recent call last):
      File "./101-generator.py", line 8, in <module>
        for line in sys.stdin:
    KeyboardInterrupt
        sleep(random.random())
    KeyboardInterrupt

>**[read_write_heap.py](read_write_heap.py)**

Script that finds a string in the heap of a running process, and replaces it.

 - Usage: `read_write_heap.py pid search_string replace_string`
 - Where `pid` is the pid of the running process
 - And strings are `ASCII`
 - The script should look only in the heap of the process.
 - On usage error, prints an error message on `stdout` and exits with status code `1`

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
