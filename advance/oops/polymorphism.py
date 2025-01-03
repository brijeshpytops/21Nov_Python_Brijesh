"""
What is polymorphism?

Polymorphism is a concept in object-oriented programming where a single interface can be used to represent different types of objects. It allows objects of different classes to be treated as objects of a common superclass.

poly - many
morphism - forms
"""

# class Math:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
    
# obj = Math()
# print(obj.add())
# print(obj.add(10, 20)) # TypeError: Math.add() missing 1 required positional argument: 'c'
# print(obj.add(10, 20, 30))

# a = 10
# a = 20
# print(a)

# class Math1:
#     def info(self):
#         return "i am from base class"
    
# class Math2(Math1):
#     def info(self):
#         print(super().info())
#         return "i am from derived class"
    
# obj = Math2()
# print(obj.info())


# operator overloading

# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, other):
#         return Math(self.a + other.a, self.b + other.b)

# obj = Math(10, 20)

# obj1 = Math(30, 40)

# obj2 = obj + obj1

# print(obj2.a)

# print(obj2.b)

