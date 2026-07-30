# 3. Medium – Search in Tuple

# Question:

# Create a tuple of programming languages.

# ("Python", "Java", "C", "C++", "JavaScript", "Go")

# Take a language as input from the user.

# If found:

# Language Found

# Else:

# Language Not Found

# Use the in operator.

languages = ("Python", "Java", "C", "C++", "JavaScript", "Go")
new = input("Enter the language : ")
if new in languages:
    print("Language Found")
else:
    print("Language Not Found")