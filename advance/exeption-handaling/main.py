"""
Exception handling in python

1. try-except block: This block allows you to handle exceptions that may occur during the execution of a program. It consists of a try block and an except block.

2. try: This block contains the code that may raise an exception.

3. except: This block contains the code that will be executed when an exception occurs in the try block. It can handle multiple exceptions by specifying a specific exception type.

4. else: This block contains the code that will be executed if no exception occurs in the try block.

5. finally: This block contains the code that will be executed regardless of whether an exception occurs or not. It is useful for releasing resources or closing files.

6. assert:
    - This statement is used to check if a condition is true. If the condition is false, an AssertionError is raised.
    - It is used for debugging and testing purposes.
    - It can be used in conjunction with the try-except block to handle specific exceptions.

7. raise: This statement is used to raise a custom exception. It can be used to create custom error messages or to create specific exceptions.

"""

# print("start")
# # print(a) # NameError: name 'a' is not defined
# print("end")

# print("start")
# try:
#     print(a)
# except Exception as err:
#     print(f"An error occurred: {err}")
# print("end")

# print("start")
# try:
#     print(a)
# except NameError:
#     print("Something is not defined")
# except Exception as err:
#     print(f"An error occurred: {err}")
# print("end")


# print("start")
# try:
#     a = 10
#     b = int(input("Enter a B: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except TypeError:
#     print("Both A and B should be numbers")
# except NameError:
#     print("Something is not defined")
# except Exception as err:
#     print(f"An error occurred: {err}")
# print("end")


# print("start")
# try:
#     a = 10
#     b = int(input("Enter a B: "))
#     res = a / b + c
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except TypeError:
#     print("Both A and B should be numbers")
# except NameError:
#     print("Something is not defined")
# except Exception as err:
#     print(f"An error occurred: {err}")
# else:
#     print(f"Result: {res}")
# finally:
#     print("This block will always execute")
# print("end")


bal = 10000
withdrow_bal = 11000

# assert withdrow_bal < bal, "Insufficent balance"

if withdrow_bal > bal:
    raise TypeError("Insufficient balance")


