# 5. Prime Number Challenge 🔥

# Ask the user to enter a number.

# Use a for-else loop to determine whether the number is prime.

# Hint: Use break when you find a divisor.

number = int(input("Enter the number : "))
while True:
    if number % 2 == 0:
        print("yes")
        break
else:
    print("No while")