# Python Packages

**Modules** and **Packages** are two mechanisms in Python that facilitate **modular programming**,
that is, they help with breaking down large chunks of code into independent, interchangeable pieces.
Each piece holds everything required to fully execute an aspect of the program's function.

There are many reasons why it is beneficial to modularise code in a large application:

- **Simplicity**: Breaking down a large program into small, well defined pieces, helps break down the overall problem into smaller, easier to handle obstacles.
This helps the programmers overcome one hurdle at a time, and have better success with incremental progress.

- **Maintainability and Debugging**: The pieces of code should be defined such that they handle a single functionality of the program or less. 
If an error occurs within that part of the program, the programmers can more easily conclude where the issue arose. 
Additionally, since the parts are interchangeable, if a better method is found that tackles the same problem, it can easily replace the previous code without a lot of tinkering or modifying the rest of the code.

- **Reusability**: The functionality in this packaged piece of code can be used again and again in the current application, or even across different applications that require the same functionality.

- **Scoping**: Packaged pieces of code define their own, separate namespace.
This means that if the application is modularised, different modules in the same application can reuse the same names for variables, without having to be concerned about name collisions.

## What is a Python module
A Python module is a file that contains Python definitions and statements. A module can be written in Python itself, or even in C and loaded dynamically at run-time. 
Python has many **built-in** modules that are integrated with the Python shell and interpreter, (like `itertools`). In short, any file that ends in `.py` can be a Python module.
They can be accessed from other files with the `import` statement.

## What is a Python package
Packages in python allow for a hierarchical structuring of the module namespace. Any folder that contains python modules, and an `__init__.py` file can be a python package. 
> *Since python 3.3 'Implicit Namespace Packages' were introduced and allow for packages to not require an `__init__.py` file.

When a package is imported with an `import` statement, it is looking for the `__init__.py` file and executes any code that is contained within. This can be useful if the package modules need to execute initialisation code.
Otherwise, the modules can be called directly with
```python
from <pkg> import <module>
```



## What is pip
`pip` is a package manager for Python. We can use `pip` to install packages.
To install with pip, use:
```bash
python3 -m pip install <package> name
```

## What is an API and why should we use it
An API, or **Application Programming Interface** is a a softaware intermediary that allows two applications to talk to each other. In a more general form, it refers to any connectivity interface to an application.
Modern APIs adhere to the REST standard, an architectural style that is designed to make web applications more standardised, saclable, performant and reliable.

APIs are useful as they provide a layer of security for applications that reside in Servers, exposed to the internet.
