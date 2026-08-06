# Write a function that returns a value inside try and prints "Cleaning Up" inside finally.

def function():
    try:
        return 90
    finally:
        print("Cleaning up !")

print(function())