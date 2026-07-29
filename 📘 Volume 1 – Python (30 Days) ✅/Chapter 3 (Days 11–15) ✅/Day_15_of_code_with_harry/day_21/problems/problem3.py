# Question 3 — Medium 🏢 (TCS Style)
# 📌 Problem: Largest of Two Numbers

# Create a function that:

# Accepts two numbers.
# Returns the larger number.
# Print the result in the main program.


def larger():
    number1 = int(input("Enter the 1st number : "))
    number2 = int(input("Enter the 2nd number : "))
    if number1 >number2:
        return number1
    else:
        return number2


larger_number = larger()
print(f"The larger number is : {larger_number}")