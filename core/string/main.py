"""
What is string?


string is a sequence of characters enclosed in single quotes, double quotes or triple quotes. It is a type of data in Python. In Python, strings are immutable, meaning they cannot be changed after they are created. The primary advantage of using strings in Python is their ability to handle and manipulate text data efficiently.
"""

str_name = 'python'
# print(type(str_name))
str_name = "python"
# print(type(str_name))
str_name = """python"""
# print(type(str_name))
str_name = '''pytohn'''
# print(type(str_name))

# print(len(str_name))


# access string with their elements
name = "python"
#   (+)(-)
# p 0 -6
# y 1 -5
# t 2 -4
# h 3 -3
# o 4 -2
# n 5 -1

# print(name)

# indexing (+/-)
# print(name[2])
# print(name[5])
# print(name[-1])
# print(name[-5])

# slicing [start:stop-1:step-1] (+/-)
name = "python"
# print(name[:])
# print(name[2:])
# print(name[2:5])
# print(name[::2])
# print(name[::-1])
# print(name[-1:-6:-1])

# using for loop

# name = "python"
# vowels = 'aeiou'
# for ch in name:
#     if ch in vowels:
#         print(ch, "is vowel")
#     else:
#         print(ch, "is consonant")

# replica
# star = "*"
# print(star*5)

# concat
# fname = "brijesh"
# lname = "gondaliya"
# fullname = fname + " " + lname
# print(fullname)

# strings methods
name = "python"
# print(dir(name))

name = "   TopS TEchNoLOGy PvT. ltD.        "
# print(name.lower())
# print(name.upper())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())

# print(name.startswith("Top"))

# print(name.endswith("gondaliya"))

# print(name.find("S"))

# print(name.index("S"))

# print(name.replace("Top", "Tech"))

# print(name.count("o") + name.count('O'))

# print(name.strip())

# print(name.lstrip())
# print(name.rstrip())


# password = "1234dsds"

# print(password.isdigit())
# print(password.isalnum())
# print(password.isalpha())

# string formatting
# book_name = "java"
# price = 343.54054
# pages = 400

# print("Book name is python and book price is 343.54054 and total pages is 400")
# print(f"Book name is {book_name} and book price is {price} and total pages is {pages}")
# print("Book name is {} and book price is {} and total pages is {}".format(book_name, price, pages))
# print("Book name is {0} and book price is {1} and total pages is {2}".format(book_name, price, pages))
# print("Book name is %s and book price is %.2f and total pages is %d" % (book_name, price, pages))
