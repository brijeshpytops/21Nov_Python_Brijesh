# Extract, search, match, replace, find - RegEx
"""

theory:

- Regular expressions (RegEx) are patterns that are used to match character combinations in strings.

- RegEx are extremely powerful tools for data manipulation and extraction.

- Python provides the 're' module to work with regular expressions.

Rules:

1. A regular expression pattern consists of various characters and special sequences.

2. Special sequences start with a backslash (\) and have specific meanings.

3. Common special sequences include:
   - \d: Matches any digit (0-9).
   - \w: Matches any alphanumeric character (a-z, A-Z, 0-9, _).
   - \s: Matches any whitespace character (space, tab, newline).
   - \D: Matches any non-digit character.
   - \W: Matches any non-alphanumeric character.
   - \S: Matches any non-whitespace character.
   - \b: Matches a word boundary.
   - \B: Matches a non-word boundary.
   - \.: Matches any period [any character].
   - \*: Matches zero or more of the preceding element.
   - \+: Matches one or more of the preceding element.
   -?: Matches zero or one of the preceding element.
   - |: Matches either the preceding or the following element.
   - [...]: Matches any character inside the brackets.
   - [^...]: Matches any character NOT inside the brackets.
   - {n}: Matches exactly n occurrences of the preceding element.
   - {n,m}: Matches at least n but not more than m occurrences of the preceding element.
   - (pattern): Groups the pattern inside the parentheses.
   - (?pattern): Creates a non-capturing group.
   - (?=pattern): Matches the pattern if it is immediately to the right of the current position.
   - (?!pattern): Matches the pattern if it is not immediately to the right of the current position.
   - (?<=pattern): Matches the pattern if it is immediately to the left of the current position.
   - (?<!pattern): Matches the pattern if it is not immediately to the left of the current position.

Modifiers:
   - \A: Matches the start of the string.
   - \Z: Matches the end of the string.
   - \b: Matches a word boundary.
   - \B: Matches a non-word boundary.
   - ^: Matches the start of the string.
   - $: Matches the end of the string.
   - (?i): Makes the matching case-insensitive.
   - (?m): Makes the matching process match across multiple lines.
   - (?s): Makes the matching process match across multiple lines, including newline characters.
   - (?x): Allows whitespace characters in the pattern to be ignored.
   - (?p<name>:pattern): Creates a named capturing group.
   - (?P=name): Matches the preceding group named 'name'.
   - (?P<!name>:pattern): Matches the preceding group named 'name' if it is not immediately to the left of the current position.

"""

import re

data = "18 to 20 cashews whole"

# Find all occurrences of the word "cashews"

# pattern1 = r'\bcashews\b'
# pattern2 = r'\d{1}\d{1}'
# result1 = re.findall(pattern1, data)
# result2 = re.findall(pattern2, data)
# print(result1 + result2)

data = ",hjasgkd mjhdgask juygsdl,a m uaswbdm, yhglkjauisd luih .xsnuibn 12-11-2024 , dlkjyhckluin 1-2-2022 jdastfkjusba xhgadas uyg 12/3/2021 jkdtakjhasbd,jsauh juy u uh 10-2/2021 kdsuyfldiskf"

# Find all occurrences of dates in the format DD/MM/YYYY.

# pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b'
# pattern = r'\b\d{2}/\d{2}/\d{4}\b'


# result = re.findall(pattern, data)

# print(result)

# search example:

data = """
1234567890
abc123
ABCabc
abcABC
"""

pattern = r'\babc\w*\b'
res = re.search(pattern, data)
# res = re.findall(pattern, data)
# print(res.span())
# print(res.group())


# replace example:

# data = "Hello, my name is Brijesh. I am 28 years old."
# pattern = r'\bB\w+\b'
# replacement = 'Samarth'
# new_data = re.sub(pattern, replacement, data)
# print(new_data)




# findall  all emails

# data = "My email is brijeshgondaliya.tops@gmail.com, and his friend's email is samarth@yahoo.com"

# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# result = re.findall(pattern, data)

# print(result)



# findall all phone numbers


# data = "My phone number is 9876543210, and his friend's phone number is 7654321098"

# pattern = r'\b\d{10}\b'

# result = re.findall(pattern, data)

# print(result)