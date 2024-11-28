"""
What are operators and operands in python?

An operator is a special character used to perform operations on operands.

Syntax:

operand1 operator operand2

Example:

num1 = 10 
num2 = 20
result = num1 + num2 # num1, num2 - operands, =, + - operators

print(result)


types of operators in python:

1. Arithmetic Operators: +, -, *, /, %, //, **
2. Assignment Operators: =, +=, -=, *=, /=, //=, %=
3. Comparison Operators: ==, !=, >, <, >=, <=
4. Logical Operators: and, or, not
5. Membership Operators: in, not in
6. Identity Operators: is, is 


"""

# 1. Arithmetic Operators: +, -, *, /, , %, //, **

# num1 = 10
# num2 = 20

# add_result = num1 + num2
# print(add_result) # 30

# sub_result = num1 - num2

# print(sub_result) # -10

# mul_result = num1 * num2

# print(mul_result) # 200

# div_result = num1 / num2

# print(div_result) # 0.5

# num1 = 10
# num2 = 2

# mod_result = num1 % num2

# print(mod_result) # 0

# div_result = num1 / num2

# print(div_result) # 5.0

# floor_div_result = num1 // num2

# print(floor_div_result) # 5

# num1 = 2
# num2 = 5

# power_result = num1 ** num2

# print(power_result) # 32

# num1 = 10
# num2 = 5

# # print(num1/num2)
# # print(num1//num2)
# print(num1**num2)

# 2. Assignment/(Shorthand) Operators: =, +=, -=, *=, /=, //=, %=

num = 10

# num = num + 20
# num += 20
# num -= 10
# num *= 2
# num /= 2
# num %= 2
# print(num)

# 3. Comparison Operators: ==, !=, >, <, >=, <=

# num1 = 10
# num2 = 20

# print(num1 == num2) # False

# print(num1 != num2) # True

# print(num1 > num2) # False

# print(num1 < num2) # True

# print(num1 >= num2) # False

# print(num1 <= num2) # True

# 4. Logical Operators: and, or, not

# A B C and or
# T T T T   T
# F T T F   T
# T F T F   T
# T T F F   T
# F F F F   F

# A not
# T F
# F T

c1 = True
# c2 = False
# c3 = 2 < 5 # True
# c4 = 10 > 100 # False

# print(c1 and c2) # False

# print(c1 or c2) # True

# print(not c1) # False


# 5. Membership Operators: in, not in

name = "Brijesh"

# print('p' in name)
# print('B' in name)
# print('b' in name)
# print('ije' in name)
# print('ije' not in name)
# print('ie' not in name)

# 6. Identity Operators: is, is not

num1 = 10
num2 = "10"
# print(num1,num2)
# print(num1 is num2)
# print(id(num1))
# print(id(num2))

# print(num1 is not num2)
