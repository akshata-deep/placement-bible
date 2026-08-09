# Mini Project — Student Marks Validator

# Build a small program that:

# Takes student marks.
# Checks whether marks are between 0 and 100.
# Uses raise ValueError for invalid marks.
# Uses try-except to handle the error.
# Displays the result if the marks are valid.


try:
    print("===== Student Marks Validator =====")
    marks = int(input("Enter the marks : "))
    if marks<0 or marks>100:
        raise ValueError("Marks should be between 0 and 100.")
    print("Valid marks!")
except Exception as e:
    print(f"Error:",e)