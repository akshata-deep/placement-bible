# Deadly Medium
# numbers = (5, 10, 15, 20, 10, 25, 10, 30)

# Print:

# Total elements
# Count of 10
# Index of 25
# Check whether 100 exists
# Print the last four elements

numbers = (5, 10, 15, 20, 10, 25, 10, 30)
print(len(numbers))
print(numbers.count(10))
print(numbers.index(25))
if 100 in numbers:
    print("yes")
else:
    print("no")
print(numbers[-4:])