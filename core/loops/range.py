"""
syntax :
range(stop+1) # default start with 0 
range(start, stop+1)
range(start, stop+1, step+1)

"""

# left to right :

# print(range(10)) # range(0, 10)
# print(range(2, 10)) # range(2, 10)

# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(2, 11))) # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(range(-5, 5))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# print(list(range(1, 11, 1))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1, 11, 2))) # [1, 3, 5, 7, 9]
# print(list(range(1, 11, 3))) # [1, 3, 5, 7, 9]

# right to left : (step value must be negative)

# print(list(range(5, -5))) # []
# print(list(range(-5, 5))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# print(list(range(5, -5, -1))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# print(list(range(5, -5, -2))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

# print(list(range(-5, 1)) + list(range(1, 6)))

# print(list(range(0, -5, -1)))
