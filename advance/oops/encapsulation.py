"""
What is encapsulation in python:

Encapsulation is a mechanism that binds together code and data into a single unit. It provides a way to hide the internal implementation details of an object and only expose the necessary functionality to the outside world.
"""

# class Person:
#     # constructor method to initialize the object attributes
#     def __init__(self, name, age, pin):
#         self.name = name # public
#         self.age = age # public
#         self.__pin = pin # private

#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#         # Private attribute can be accessed using a method
#         print(f"Pin: {self._Person__pin}")

# n = input("Enter a name: ")
# a = int(input("Enter an age :"))
# p = int(input("Enter a pin: "))

# Creating an object of the Person class and accessing its attributes and methods
# obj = Person(n, a, p)

# Accessing the attributes and methods of the object
# print(f"Name: {obj.name}")
# print(f"Age: {obj.age}")
# We can't access the private attribute directly
# print(f"Pin: {obj.__pin}")

# obj.info() # Accessing the public method of the class

# To access the private attribute, we can use a method
# print(f"Pin {obj._Person__pin}") # name mangling: _ClassName__varname


# getter and setter method:

# class Person:
#     def __init__(self, name, age, pin):
#         self.__name = name
#         self.__age = age
#         self.__pin = pin

#     # getter method for name attribute
#     def get_name(self):
#         return self.__name
    
#     # setter method for name attribute
#     def set_name(self, name):
#         self.__name = name


# n = input("Enter a name: ")

# a = int(input("Enter an age :"))

# p = int(input("Enter a pin: "))

# person = Person(n, a, p)

# print(f"Before updating name: {person.get_name()}")

# person.set_name("New Name: samarth")

# print(f"After updating name: {person.get_name()}")


