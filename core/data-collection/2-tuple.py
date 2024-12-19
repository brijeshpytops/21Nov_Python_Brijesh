"""
Tuple in python: Ordered, immutable, duplicate values are allowed, indexing, slicing

syntax:

tuple_name = ()
tuple_name = tuple()
comma_tuple_name = 10,3,45,
"""

# nums = ()
# print(type(nums))
# print(len(nums))

# nums = 1,2,3,4,5
# nums = 1,
# print(type(nums))

# nums = (1,2,3,4,5,1,2,3,4,5)
# print(nums)

# indexing 

nums = (1,2,3,4,5)
# print(nums[0])
# print(nums[-1])

# slicing
# print(nums[::-1])
# print(nums[1:])
# print(nums[:3])


# nums[0] = 111 # TypeError: 'tuple' object does not support item assignment
# print(nums)

nums = 1,2,3,1,2,1,1,2,1,2,1,3,55

# print(dir(nums))

# 'count', 'index'

# print(nums.count(1))
# print(nums.index(55))


