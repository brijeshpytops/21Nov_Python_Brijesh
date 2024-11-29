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

num = 5
for row in range(1, num+1):
    for col in range(1, num+1):
        print("*", end=" ")
    print()