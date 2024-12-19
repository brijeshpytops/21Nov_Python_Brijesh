"""
Dictionary : ordered, mutable, duplicate keys are not allowed

theory:

- Dictionaries are unordered collections of key-value pairs.

- Dictionaries are denoted by curly braces ({}) and are used to store key-value pairs.

- The keys in a dictionary are unique, and they must be immutable (like strings, numbers, or tuples).

- The values in a dictionary can be of any data type, including lists, dictionaries, and even other dictionaries.


syntax:
- Dictionaries can be created using the {} syntax or by using the dict() function.

dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3,
}

dict_name = dict()
"""

# Create a dictionary

# my_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(my_dict)
# print(type(my_dict))

# print(len(my_dict))

# print(my_dict["city"])

# Update a value

# my_dict["age"] = 35

# print(my_dict)

# delete key-value pair

# del my_dict["age"]

# del my_dict

# print(my_dict) # NameError: name 'my_dict' is not defined

fruits = {
    "apple": 10,
    "banana": 5,
    "cherry": 8,
    "orange": 7,
    "grape": 3,
    "mango": 2,
    "kiwi": 4,
    "kiwi": 10
}

# print(fruits["banana"])
# print(fruits)

# print(dir(fruits))



# fruits.clear() # {}

# new_fruites = fruits.copy() # {'apple': 10, 'banana': 5, 'cherry': 8, 'orange': 7, 'grape': 3, 'mango': 2, 'kiwi': 10}

# print(new_fruites)

# vegs = [
#     "potato",
#     "carrot",
#     "onion",
#     "broccoli",
#     "spinach",
#     "cabbage",
#     "cauliflower",
#     "zucchini"
# ]

# price = 100

# veg_dict = {}

# print(veg_dict.fromkeys(vegs, price)) # {'potato': 100, 'carrot': 100, 'onion': 100, 'broccoli': 100, 'spinach': 100, 'cabbage': 100, 'cauliflower': 100, 'zucchini': 100}

fruits = {
    "apple": 10,
    "banana": 5,
    "cherry": 8,
    "orange": 7,
    "grape": 3,
    "mango": 2,
    "kiwi": 4,
    "kiwi": 10
}

# print(fruits.get('orange')) # 7
# print(fruits.keys())

# for key in fruits.keys():
#     print(key)
# for value in fruits.values():
#     print(value)

# for key, value in fruits.items():
#     print(key, value)

# print(fruits.pop('kiwi')) # 10
# print(fruits.popitem()) # ('kiwi', 10)

car = {
    "brand": "Tesla",
    "model": "Model X",
    "year": 2021,
    "color": "red"
}

# car.setdefault("color", "black")
# car.setdefault("year", 2000)
# print(car)

new_car_details = {
    "speed": "200k/h",
    "fuel_type": "electric",
    "driver": {
        "name": "John Doe",
        "age": 30,
        "gender": "male"
    }
}

# car.update(new_car_details)

# print(car) # {'brand': 'Tesla', 'model': 'Model X', 'year': 2021, 'color': 'red', 'speed': '200k/h', 'fuel_type': 'electric', 'driver': {'name': 'John Doe', 'age': 30, 'gender': 'male'}}


# users = []
# start = 0
# end= 3
# while  start <= end:
#     start+=1
#     user = {
#         "user_id": start,
#         "name": input("Enter a name: "),
#         "age": int(input("Enter an age: ")),
#         "email": input("Enter an email: "),
#         "address": input("Enter an address: "),
#         "phone": input("Enter a phone number: ")
#     }
#     users.append(user)

# print(users)


# users = [{'user_id': 1, 'name': 'brijesh', 'age': 28, 'email': 'brijesh@gmail.com', 'address': 'surat', 'phone': '7879879879'}, {'user_id': 2, 'name': 'raj', 'age': 24, 'email': 'raj@gmail.com', 'address': 'rajkot', 'phone': '7568768768'}, {'user_id': 3, 'name': 'jay', 'age': 67, 'email': 'jay@gmail.com', 'address': 'ahmedabad', 'phone': '54765786576'}, {'user_id': 4, 'name': 'ravi', 'age': 45, 'email': 'ravi@gmail.com', 'address': 'mumbai', 'phone': '6587568768'}]

# print(users)
# print(users[0])

# for user in users:
#     print(user['name'])