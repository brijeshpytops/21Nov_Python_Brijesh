# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

num = 5
for row in range(1, num+1):
    for col in range(1, num+1):
        print("*", end=" ")
    print()



# * 
# * * 
# * * * 
# * * * * 
# * * * * *

num = 5

for row in range(1, num+1):
    for col in range(1, row+1):
        print("*", end=' ')
    print()

# * * * * *
# * * * * 
# * * * 
# * * 
# * 


num = 5
for row in range(1, num+1):
    for col in range(1, num-row+2):
        print("*", end=" ")
    print()


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# * * * * *
#   * * * * 
#     * * * 
#       * * 
#         * 


# num = 5

# for row in range(1, num+1):
#     for col in range(1, row):
#         print(" ", end=' ')
#     for col in range(1, num-row+2):
#         print("*", end=" ")
#     print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# * * * * 
# * * * 
# * * 
# * 

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("*", end=" ")
#     print()

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *
#   * * * * 
#     * * * 
#       * * 
#         * 

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


# 0
# 1 1
# 0 0 0
# 1 1 1 1
# 0 0 0 0 0
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         if row % 2 == 0:
#             print("1", end=' ')
#         else:
#             print("0", end=' ')
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


num = 5
for row in range(1, num+1):
    for col in range(1, row+1):
        print(row, end=" ")
    print()


# A
# B B
# C C C
# D D D D
# E E E E E


num = 5
for row in range(1, num+1):
    for col in range(1, row+1):
        print(chr(row + 64), end=" ")
    print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


num = 5
g_var = 1
for row in range(1, num+1):
    for col in range(1, row+1):
        print(g_var, end=" ")
        g_var += 1
    print()

# A
# B C
# D E F
# G H I J
# K L M N O

num = 5
g_var = 1
for row in range(1, num+1):
    for col in range(1, row+1):
        print(chr(g_var + 64), end=" ")
        g_var += 1
    print()


# 0
# 0 1
# 0 1 0
# 0 1 0 1
# 0 1 0 1 0

for row in range(1, num+1):
    for col in range(1, row+1):
        if col % 2 == 0:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()



#         * 
#       * * * 
#     * * * * *
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * *
#         * 


# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print(" ", end=" ")
#     for col in range(1, row+1):
#         print("*", end=' ')
#     for col in range(1, row):
#         print("*", end=' ')
#     print()

# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end=' ')
#     for col in range(1, num-row+1):
#         print("*", end=" ")
#     for col in range(1, num-row):
#         print("*", end=" ")
#     print()