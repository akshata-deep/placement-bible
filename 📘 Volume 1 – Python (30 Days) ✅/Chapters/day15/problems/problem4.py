# Problem 4 – Grade System

# Take a grade from the user.

# A
# B
# C
# D

# Print:

# A → Excellent
# B → Good
# C → Average
# D → Needs Improvement
# Default → Invalid Grade



grade = input("Enter the grade :")



match grade:

    case "A":

        print("A → Excellent")

    case "B":

        print("B → Good")

    case "C":

        print("C → Average")
    case "D":

        print("D → Needs Improvement")

    case _:

        print("invalid grade!")