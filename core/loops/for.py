"""
What is for loop in python?

A for loop is a control flow statement that allows you to iterate over a sequence of items, such as a list, tuple, or string.

Syntax:

for variable in sequence:
    statement
"""

# name = "python"
# for ch in name:
#     print(ch)

# name = "python"
# for ch in name:
#     print(ch, end="")

# name = "python"

# chs = iter(name)

# print(next(chs))
# print(next(chs))
# print(next(chs))
# print(next(chs))
# print(next(chs))
# print(next(chs))
# print(next(chs))



# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print("*", end=" ")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# num = 5

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()


# * * * * *
# * * * * 
# * * * 
# * * 
# * 
# 1 - 5 = 6
# 2 - 4 = 6
# 3 - 3 = 6
# 4 - 2 = 6
# 5 - 1 = 6

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+2):
#         print("*", end=" ")
#     print()


# - - - - * 
# - - - * * 
# - - * * * 
# - * * * * 
# * * * * *


# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()


# num = 5

# for row in range(1, num+1):
#     for col in range(1, row):
#         print(" ", end=' ')
#     for col in range(1, num-row+2):
#         print("*", end=" ")
#     print()


num = 5

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("*", end=" ")
#     print()


# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end=' ')
#     for col in range(1, num-row+1):
#         print("*", end=" ")
#     print()

# num = 5
# g_var = 1
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(g_var + 64), end=" ")
#         g_var += 1
#     print()


# for row in range(1, num+1):
#     for col in range(1, row+1):
#         if col % 2 == 0:
#             print("1", end=' ')
#         else:
#             print("0", end=' ')
#     print()

num = 5
for row in range(1, num+1):
    for col in range(1, num-row+1):
        print(" ", end=" ")
    for col in range(1, row+1):
        print("*", end=' ')
    for col in range(1, row):
        print("*", end=' ')
    print()

for row in range(1, num+1):
    for col in range(1, row+1):
        print(" ", end=' ')
    for col in range(1, num-row+1):
        print("*", end=" ")
    for col in range(1, num-row):
        print("*", end=" ")
    print()