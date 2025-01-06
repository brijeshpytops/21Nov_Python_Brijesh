"""
file handling in python:

# opening a file

file = open('sample.txt', 'w')

# writing into the file

file.write('Hello, this is a sample text.')

# closing the file

file.close()

# reading the file

file = open('sample.txt', 'r')

content = file.read()

# closing the file

file.close()

print(content)
"""
# create new file
# open('example.txt', 'w')
# open('example1.txt', 'x')
# open('example2.txt', 'a')


# file = open('example.txt', 'w')
# file.write(input("Enter a something: "))
# file.close()
# file.write(input("Enter a something: "))




# file = open('example.txt', 'r')
# print(file.read())
# print(file.read(9))

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())
# file.close()

# file = open('example.txt', 'w')
# lines = ['This is a line - 1\n', 'This is a line - 2\n', 'This is a line - 3\n', 'This is a line - 4\n', 'This is a line - 5\n', 'This is a line - 6']
# file.writelines(lines)
# file.close()

# file = open('example.txt', 'a')
# file.write('\nThis is a line - 8')
# file.close()

# file = open('example.txt', 'r')
# print(file.tell())
# print(file.seek(9))
# print(file.tell())

import os
# os.rename('example.py', 'test.py')
# os.remove('test.py')

# file = open('example.py', 'w')
# file.write("print('this is a created by file handling')")
# os.system('py example.py')