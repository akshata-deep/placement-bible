# Q7 — Program Continues

# Create a program where an error occurs, but after handling the error, another line prints:

# Program continues

try:
    numbers = [10, 20, 30, 40]
    indexing_num = int(input("Enter the indexs value: "))
    print(f"{numbers[indexing_num]}")
except Exception as e:
    print(e)

print("Program continues")