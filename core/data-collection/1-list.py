"""
list in python: Ordered, mutable, duplicate values are allowed, indexing, slicing

theory:

- List is a collection of items in a particular order.

- Lists are mutable, meaning their elements can be changed after they are created.

- Lists are denoted by square brackets ([]).

- Lists can contain different types of data, including strings, integers, floats, and even other lists.

- Lists can be nested, meaning one list can contain another list as an element.

- Lists in Python support indexing and slicing.

- Lists in Python support methods like append(), insert(), remove(), pop(), extend(), count(), reverse(), copy(), index(), clear(), and sort().

- Lists in Python support the len() function to get the number of elements in a list.

- Lists in Python support the in operator to check if an item is present in a list.

- Lists in Python support the + operator to concatenate two lists.

- Lists in Python support the * operator to repeat a list a specified number of times.

- Lists in Python support the del keyword to delete an item from a list.

- Lists in Python support the min() and max() functions to get the minimum and maximum values in a list.


syntax:

list_name = [element1, element2, element3,...]
list_name = list()
"""

# nums = [1,2,3,4,5]
# print(type(nums))
# print(len(nums))

# mix_list = [12, 23.56, 'python', 'jhh']

# print(mix_list)


# Access elements of list

items = [
    'apple',
    'banana',
    'cherry',
    'date',
    'elderberry'
]
# indexing (+/-)

# print(items[0])  # apple

# print(items[2])  # cherry

# print(items[-1])  # elderberry

# print(items[-3])  # cherry

# Slicing [start:stop-1:step-1] (+/-)

# print(items[1:4])  # ['banana', 'cherry', 'date']

# print(items[:3])  # ['apple', 'banana', 'cherry']

# print(items[2:])  # ['cherry', 'date', 'elderberry']

# print(items[-3:])  # ['cherry', 'date', 'elderberry']

# print(items[::2])  # ['apple', 'cherry', 'elderberry']

# print(items[::-1])  # ['elderberry', 'date', 'cherry', 'banana', 'apple']

# Update list

# items[0] = "mango"

# del items[0]
# print(items)

# mummy = ['milk', 'tomato', 'potato', 'onion']
# aunty = ['tomato', 'potato', 'onion']
# my_list = ['drink', 'pen', 'book']
# sister = ['chocolate']

# concat
# print(mummy + aunty + my_list + sister)

# REPLICA
# sister = sister*3

# print(sister)

# LIST METHODS

items = [
    'apple',
    'banana',
    'cherry',
    'date',
    'elderberry'
]

new_items = [
    'grape',
    'mango'
]

# add
# items.append(new_items) # ['apple', 'banana', 'cherry', 'date', 'elderberry', ['grape', 'mango']]
# items.extend(new_items) # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'grape', 'mango']
# items.insert(1, new_items) # ['apple', ['grape', 'mango'], 'banana', 'cherry', 'date', 'elderberry']

# del

# items.remove('elderberry')
# items.pop() # default remove laste value of list
# items.pop(2)
# items.clear()

# mix
# print(items.index('date'))

# items.reverse()
# items.sort()
# items.sort(reverse=True)

# print(items)

# nums = [1,1,2,2,3,4,54,6,7,8,8,9,9,0,0,1,1,2,1,2,1,1,1,1]

# print(nums.count(1))

# num1 = [1,2,3,4]
# copy_num1 = num1.copy()
# print(copy_num1)

# nums = [1,2,4,5,6,8,9,5,7,4,66,365,2,5,8,3,55,6,8,6]

# print(max(nums))

# print(min(nums))
# print(sum(nums)/len(nums))

# nested_list = [1,2,[3,4, [[5,6],7,8]]]

# print(nested_list[2])
# print(nested_list[2][2])
# print(nested_list[2][2][0])