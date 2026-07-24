# 📌 Syntax
# String Creation
# name = "Akshata"
# name = 'Akshata'
# text = """This is
# a multiline
# string"""
# Indexing
# name[0]
# name[-1]
# Slicing
# name[start:end]

# Example

# name = "Python"

# print(name[1:4])

# Output

# yth
# Negative Indexing
# name[-1]

# Last character

# name[-2]

# Second last character

# Length
# len(name)

# Returns total number of characters.

# 📌 Rules
# Rule 1

# Index starts from 0

# Python

# P  y  t  h  o  n
# 0  1  2  3  4  5
# Rule 2

# Negative index starts from -1

# Python

# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1
# Rule 3

# Slicing includes the start index.

# name[1:4]

# Starts from index 1

# Rule 4

# Ending index is excluded.

# name[1:4]

# Returns

# yth

# Not

# ytho
# Rule 5

# len() counts spaces also.

# Example

# len("Hi All")

# Output

# 6
# Rule 6

# Indexing returns one character.

# name[2]
# Rule 7

# Slicing returns a substring.

# name[2:5]
# Rule 8

# Slicing never gives IndexError.

# name[100:]

# Output

# ""
# Rule 9

# Indexing can give IndexError.

# name[100]

# Output

# IndexError
# 📌 Common Mistakes

# ❌ Forgetting that the ending index is excluded.

# ❌ Confusing indexing with slicing.

# ❌ Using name[10] instead of name[10:].

# ❌ Forgetting negative indexing starts from -1, not 0.

# ❌ Thinking Python has a separate character data type. (It doesn't. A single character is still a str.)

# 📌 Interview Tips

# ✅ Draw the indexes before solving slicing questions.

# Example

# Python

# 0 1 2 3 4 5

# ✅ Remember:

# Indexing → One character
# Slicing → Multiple characters

# ✅ len() returns the number of characters, including spaces.

# ✅ name[:] returns the entire string.

# 📌 Shortcuts
# First Character
# name[0]
# Last Character
# name[-1]
# First 3 Characters
# name[:3]
# Last 3 Characters
# name[-3:]
# Complete String
# name[:]
# Length
# len(name)


x = '7'
print(x*2)