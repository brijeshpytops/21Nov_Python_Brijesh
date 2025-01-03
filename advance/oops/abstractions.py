"""
What is abstract class:

An abstract class is a class that contains one or more abstract methods. Abstract methods are methods that have no implementation but are defined in the class.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass

# obj = Animal() #  Can't instantiate abstract class Animal without an implementation for abstract method 'voice'

class Dog(Animal):
    def voice(self):
        return "Woof!"

class Cat(Animal):
    def voice(self):
        return "Meow!"
    
obj = Dog()
print(obj.voice())

obj = Cat()
print(obj.voice())