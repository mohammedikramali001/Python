#  <center>  <ins> <em>  Python fact finder
![GIF](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2ZsdGVkbTVqMGowMTVmaGZiNngzdHJmMmQ2eWhpY2N1ZHk2dzRrYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.gif)
---
## Define a list and tuple in Python

List and Tuple are built-in container types defined in Python. 
Objects of both these types can store different other objects that are accessible by index. List as well as tuple is a sequence data type, just as string. List as well as tuple can store objects which need not be of same type.

> example of list: fruits = ["apple", "banana", "cherry"]
> print(fruits)

> example of tuple: fruits = ("apple", "banana", "cherry")
> print(fruits)


## What is a namespace in python?

In Python, a namespace is a system that has a unique name for each and every object. An object might be a variable or a method. e.g. Built-In Namespace, Global Namespace, Local Namespace

## what is the difference between a local variable and global variable

#### Global variables:
Global variables are declared outside of any function or at the top level of a script.
Their global scope makes them accessible throughout the program.
A program's global variables are created when it starts and remain in memory until the program ends.
Any function within the program can access and modify global variables.
Example: Global variable


> global_var1 = 250  # This is a global variabledef function_with_global_var():    print("Global variable value:", global_var1)function_with_global_var()  # Output: Global variable value: 250

####Local variables:
A local variable is one that is declared within a function and has a local scope.
They are accessible only within the function in which they are defined.
Local variables are created when the function is called and destroyed when it exits.
Local variables cannot be accessed from outside the function.
Example: Local variable:


> def function_with_local_var():    local_var = 45  # This is a local variable    print("Local variable value:", local_var)
function_with_local_var()  # Output: Local variable value: 45print(local_var)  # Error: NameError - local_var is not defined

## What is an IDE?
An integrated development environment (IDE) is a software application that helps programmers develop software code efficiently. It increases developer productivity by combining capabilities such as software editing, building, testing, and packaging in an easy-to-use application. Just as writers use text editors and accountants use spreadsheets, software developers use 
IDEs to make their job easier.

####IDE Examples
 
* [pycharm](https://www.jetbrains.com/pycharm/)
* [jupyter](https://jupyter.org/)
* [IDLE](https://docs.python.org/3/library/idle.html)
* [visual studio code](https://code.visualstudio.com/)
* [spyder](https://www.spyder-ide.org/)

## What are modules in python?
To create a module just save the code you want in a file with the file extension .py:

>Example:
Get your own Python Server
Save this code in a file named mymodule.py
def greeting(name):
    print("Hello, " + name)

Use a Module
Now we can use the module we just created, by using the import statement:
Example:

> Import the module named mymodule, and call the greeting function:
import mymodule
mymodule.greeting("Jonathan")

## What is the difference between an array and a list

In Python, both lists and arrays are used to store data. They are similar in that they can both store items in an ordered manner and allow indexing, slicing, and iterating. However, there are some key differences between them:
 
> Declaration: Lists are built-in data structures in Python, so you don’t need to import any module to declare a list. On the other hand, arrays need to be declared using the array module or the NumPy package.
 
>Data Types: Lists can consist of elements belonging to different data types. In contrast, arrays in Python (especially when using the array module) can only consist of elements belonging to the same data type.
 
>Memory and Performance: Arrays can store data very compactly and are more efficient for storing large amounts of data. Arrays also perform better when it comes to numerical operations.

## What are operators

Operators in Python are special symbols or keywords that are used to perform operations on values or variables. They are used to manipulate data, perform mathematical and logical operations, and make decisions in your Python code. Python provides a wide range of operators for different purposes. 
> Arithmetic Operator
a = 10
b = 20
print("Addition: ", a + b)

``` 

```
