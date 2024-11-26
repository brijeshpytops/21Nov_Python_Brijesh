"""
What are datatypes in python?

Datatypes are the different types of data that can be stored in variables in Python. Python has many built-in datatypes, including:

- Integers (int): These are whole numbers, such as 1, 2, 3, -4, -5 etc.

- Floating-point numbers (float): These are numbers with a decimal point, such as 1.5, 2.3, 3.14, -3.5, -78.5 etc.

- Complex numbers (complex): These are numbers with real and imaginary parts, such as 1+2j, -3+4j, 5-6j, -7-8j etc.

- Strings (str): These are sequences of characters, such as "Hello", "Python", "123", "abc" etc.

- Booleans (bool): These are binary values, either True or False.

- Lists (list): These are ordered collections of items, such as [1, 2, 3, 4, 5], ["apple", "banana", "cherry"], [True, False, True, False] etc.

- Tuples (tuple): These are ordered collections of items, similar to lists, but they are immutable, meaning they cannot be changed after they are created. For example, (1, 2, 3, 4, 5)

- Sets (set): These are unordered collections of items, similar to lists, but they do not allow duplicate values. For example, {1, 2, 3, 4, 5}, {"apple", "banana", "cherry"} etc.

- Dictionaries (dict): These are unordered collections of key-value pairs, such as {"name": "John", "age": 30, "city": "New York"}.

- Ranges (range): These are sequences of numbers, similar to lists or tuples, but they are generated on the fly and do not store all the values in memory. For example, range(1, 10) generates the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9.

- None: This is a special value in Python that represents no value or no object. It is used to indicate that a variable does not have a value.
"""

# integer = 10
# print(type(integer)) # <class 'int'>

# float_number = 10.5

# print(type(float_number)) # <class 'float'>

# complex_number = 10 + 2j

# print(type(complex_number)) # <class 'complex'>

# string = "Hello, World!"

# print(type(string)) # <class 'str'>

# boolean = True

# print(type(boolean)) # <class 'bool'>

# list_of_numbers = [1, 2, 3, 4, 5]

# print(type(list_of_numbers)) # <class 'list'>

# tuple_of_numbers = (1, 2, 3, 4, 5)

# print(type(tuple_of_numbers)) # <class 'tuple'>

# set_of_numbers = {1, 2, 3, 4, 5}

# print(type(set_of_numbers)) # <class 'set'>

# dictionary_of_items = {
#     "name": "John", 
#     "age": 30, 
#     "city": "New York"
# }

# print(type(dictionary_of_items)) # <class 'dict'>

# range_of_numbers = range(1, 10)

# print(type(range_of_numbers)) # <class 'range'>

# none_value = None

# print(type(none_value)) # <class 'NoneType'>


# Type conversion

# implicit type conversion

num1 = 10
num2 = 20.98

print(type(num1 + num2)) 

# explicit type conversion

# num_int = 10

# num_str = str(num_int)

# print(type(num_str)) # <class'str'>
# num_str = "10"

# num_int = int(num_str)

# print(type(num_int)) # <class 'int'>

