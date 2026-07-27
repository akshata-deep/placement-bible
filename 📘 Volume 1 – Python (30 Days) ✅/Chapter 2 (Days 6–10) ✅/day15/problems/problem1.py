# Problem 1 – Day of the Week

# Take a number (1–7) from the user.

# Using match-case, print the day.

# Example:

# Input: 1
# Output: Monday



day_number = int(input("Enter the number of the day :"))

match day_number:
    case 1:
        print("Monday!")
    case 2:
        print("Tuesday!")
    case 3:
        print("Wednesday!")
    case 4:
        print("Thursday!")
    case 5:
        print("Friday!")
    case 6:
        print("Satarday!")
    case 7:
        print("Sunday!")
    case _:
        print("Invalid")