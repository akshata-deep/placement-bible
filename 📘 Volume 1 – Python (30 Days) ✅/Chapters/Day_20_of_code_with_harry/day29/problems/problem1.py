# Q1 — Easy

# Create a function called:

# square()

# Add a proper docstring explaining:

# what input it takes
# what it returns

# Then print its docstring using .__doc__.


def square():
    ''' it will take 2 numbers a and b and print the sum of that '''
    a = int(input("Enter the number 1 : "))
    b = int(input("Enter the number 2 : "))
    c = a + b 
    print(f"Sum : {c}")

print(square.__doc__)