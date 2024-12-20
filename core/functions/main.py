"""
What is function in python?

A function is a block of code that performs a specific task. It takes input, performs some operations, and produces output.

Syntax:

def function_name(arguments/parameteres):
    code block

Function call:

function_name(arguments_values)
"""

# Example-1: Define a simple function to add two numbers

# num1 = 10
# num2 = 20

# total= num1+num2


# def add_numbers(num1, num2):
#     print(num1 + num2)
#     return num1 + num2

# add_numbers(10, 20)
# add_numbers(30, 40)
# add_numbers(50,60)

# total = add_numbers(10,20)
# print(total)

# Types of parameters in python
# 1] positional parametes
# 2] default/keyword parameters
# 3] variable length parameters

# 1]  

# def add(a,b,c):
#     return a+b+c

# print(add(1,2,3))
# print(add(1,2,3,44, 55))
# print(add(1,2))

# 2] 

# def bill(gst_pr, tomato=20, book=100):
#     return tomato + book - gst_pr

# print(bill(10, 40, 200))

# 3] variable length parameters
# *args
# **kwargs

# def add(*nums):
#     return sum(nums)

# print(add(1,2,3,4,5,5,6,100,120))

# def bill(**products):
#     total = 0
#     for item, price in products.items():
#         total += price
#         print(f"{item}: {price}")

#     return total

# print(bill(tomato=20, book=100, milk=50, potato=30))

# Generator
# def nums():
#     yield 1
#     yield 2
#     yield 3

# nums_ = nums()
# print(next(nums_))
# print(next(nums_))
# print(next(nums_))
# print(next(nums_))