# 4. raise + try-except

# Create a program where you manually raise ValueError, then handle it using except.


try:
    a = int(input("Enter the number"))
    if a == 1:
        raise ValueError
except Exception as e:
    print(e)