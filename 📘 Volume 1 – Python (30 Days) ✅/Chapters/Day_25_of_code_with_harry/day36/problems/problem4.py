# Q4 — List Index

# Given:

# numbers = [10, 20, 30, 40]

# Ask the user for an index and print the corresponding element.

# Handle IndexError.
try:
    numbers = [10, 20, 30, 40]
    indexing_num = int(input("Enter the indexs value: "))
    print(f"{numbers[indexing_num]}")
except IndexError:
    print("Index Error")
except ValueError:
    print("ValueError")

