# Create a new list using list comprehension that:

# Keeps only the names that have more than 5 letters.
# Converts those names to UPPERCASE.


names = ["akshata", "rahul", "john", "asha", "priyaqqqq"]
uppercase_5 = [u.upper() for u in names if len(u)>5]
print(uppercase_5)