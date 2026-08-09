# 3. Custom message

# Create a program that raises:

# Value should be between 5 and 9

# when the input is invalid.

a = int(input("Enter the num : "))
if a<5 or a>9:
    raise ValueError("Value should be between 5 and 9")
print("Done")
