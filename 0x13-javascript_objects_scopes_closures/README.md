# Holberton School Project

>This repo is part of the Holberton School curriculum. Is the second project related with JS.

## JavaScript - Objects, Scopes and Closures

Here the OOP in JS is introduced to students!

---

## In this REPO:

>**[0-rectangle.js](0-rectangle.js)**

Empty class `Rectangle` that defines a rectangle:. Usage: `Rectangle = require('./0-rectangle')`.

Here how the script works:

    guillaume@ubuntu:~/0x13$ cat 0-main.js
    #!/usr/bin/node
    const Rectangle = require('./0-rectangle');

    const r1 = new Rectangle();
    console.log(r1);
    console.log(r1.constructor);
    guillaume@ubuntu:~/0x13$ ./0-main.js
    Rectangle {}
    [Function: Rectangle]
    guillaume@ubuntu:~/0x13$ 

>**[1-rectangle.js](1-rectangle.js)**

Class `Rectangle` that defines a rectangle with a Width and a Height:. Usage: `Rectangle = require('./1-rectangle')`.

Here how the script works:


    guillaume@ubuntu:~/0x13$ cat 1-main.js
    #!/usr/bin/node
    const Rectangle = require('./1-rectangle');

    const r1 = new Rectangle(2, 3);
    console.log(r1);
    console.log(r1.width);
    console.log(r1.height);

    const r2 = new Rectangle(2, -3);
    console.log(r2);
    console.log(r2.width);
    console.log(r2.height);

    const r3 = new Rectangle(2);
    console.log(r3);
    console.log(r3.width);
    console.log(r3.height);

    guillaume@ubuntu:~/0x13$ ./1-main.js
    Rectangle { width: 2, height: 3 }
    2
    3
    Rectangle { width: 2, height: -3 }
    2
    -3
    Rectangle { width: 2, height: undefined }
    2
    undefined
    guillaume@ubuntu:~/0x13$

---

### Author

All the code in this REPO was made by **Luis Patiño** in 2021, as part of Holberton School developer training.

---

<div>
<div align="center">
<img display="block" alt="Holberton Logo" width="50%" src="https://www.holbertonschool.com/holberton-logo.png">
</div>
<p align="center"><b>2020</b></p>
</div>

---
