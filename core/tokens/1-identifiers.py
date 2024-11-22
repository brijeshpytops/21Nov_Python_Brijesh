"""
What is identifiers in python?

They are used to name variables, functions, classes, and modules.

# A Identifiers must be unique.

# A Identifier can be a combination of letters[a-z, A-Z], digits[0-9], or underscores[_].

# A Identifier cannot start with a digit.
Example: 1level - false, level_1 - True

# A Identifier is case sensitive.
Example: FirstName, firstname,FIRSTNAME

# A Identifier should not be a keyword.
Example: for, while, if, else, elif, print, return, class, def, in, not, and, or, is, return, True, False, None

# A Identifier should not contain any special characters or spaces.
Example: @hello, #bollywood
"""

# Valid identifiers:

level = 10
level_1 = 100
firstName = "John"
FirstName = "John"
_level = 10

# Invalid identifiers:

1level = 10  # Starts with a digit
level 1 = 100  # Contains a space
@hello = 10  # Contains special characters
1#bollywood = 10  # Contains special characters and spaces
for = 30 # you can not use keywords as an identifiers.