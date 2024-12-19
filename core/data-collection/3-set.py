"""
set: Unordered, mutable, duplicate values not allowed, unidexed, slicing not allowed

syntax:

set_name = {element1, element2, element3,...}
set_name = set()

"""

# nums = [1,2,3,1,4,1,2,3,1,3,4,45,5,5,6,7,7,]
# print(set(nums))

# nums = {1,2,3,4,5}
# print(type(nums))

# print(nums[0])

# nums.add(6)
# print(nums)

nums = {1,2,3,4,5}
nums = frozenset(nums)

# print(nums[0])

# nums[0] = 333
# print(nums)

