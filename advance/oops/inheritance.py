"""
Inheritance in python:

Inheritance allows a class to inherit properties and methods from another class. The class that inherits is called the derived class, and the class that is inherited is called the base class.

types of inheritance:

1. Single inheritance: In this case, a derived class inherits from only one base class.

2. Multiple inheritance: In this case, a derived class inherits from multiple base classes.

3. Multilevel inheritance: In this case, a derived class inherits from a base class, and that base class in turn inherits from another base class.

4. hierarchical:

In this case, a derived class inherits from a base class, and the base class in turn inherits from another base class.

5. hybrid:

In this case, a derived class inherits from a base class, and that base class in turn inherits from multiple other classes.
"""

# single inh:

# parent/base class
# class A:
#     def a(self):
#         print("This is class A")

# # child/derived class

# class B(A):
#     def b(self):
#         print("This is class B")

# obj = B()
# obj.a()
# obj.b()

# multiple inh:

# parent/base class

# class A:
#     def a(self):
#         print("This is class A")

# # child/derived class

# class B:
#     def b(self):
#         print("This is class B")

# class C(A, B):
#     def c(self):
#         print("This is class C")

# obj = C()
# obj.a()
# obj.b()
# obj.c()



# multilevel inh:

# parent/base class

# class A:
#     def a(self):
#         print("This is class A")

# # child/derived class
# class B(A):
#     def b(self):
#         print("This is class B")

# # grandchild/derived class
# class C(B):
#     def c(self):
#         print("This is class C")

# obj = C()
# obj.a()
# obj.b()
# obj.c()



# hierarchical inh:

class Shape:
    def shape(self):
        print("This is a shape")

class Shape2D(Shape):
    def shape2D(self):
        print("This is a 2D shape")

class Circle(Shape2D):
    def circle(self):
        print("This is a circle")

class Rect(Shape2D):
    def rect(self):
        print("This is a rectangle")


class Shape3D(Shape):
    def shape3D(self):
        print("This is a 3D shape")

class Cube(Shape3D):
    def cube(self):
        print("This is a cube")

class Sphere(Shape3D):
    def sphere(self):
        print("This is a sphere")

# c = Circle()

# c.shape()
# c.shape2D()
# c.circle()


# c = Cube()

# c.shape()

# c.shape3D()

# c.cube()




# hybrid inh:

class Animal:
    def animal(self):
        print("This is an animal")

class Dog(Animal):
    def dog(self):
        print("This is a dog")

class Cat(Animal):
    def cat(self):
        print("This is a cat")

class Bird(Animal):
    def bird(self):
        print("This is a bird")

d = Dog()
d.animal()
d.dog()

c = Cat()
c.animal()
c.cat()

b = Bird()
b.animal()
b.bird()
