# 6. Marks validation

# Ask for marks.

# Valid range:

# 0–100

# If the user enters anything outside this range, raise a ValueError.

marks = int(input("Enter the marks : "))
if marks<0 or marks>100:
    raise ValueError("no range")
print("done")