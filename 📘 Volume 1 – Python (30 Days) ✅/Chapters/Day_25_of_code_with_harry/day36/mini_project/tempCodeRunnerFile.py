try:
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
except ValueError:
        print("ValueError! Please enter integers only.\n")

print("\n===== Safe Calculator =====")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n")

while True:
    try:
        option = int(input("Enter the option : "))
        if option == 1:
            print(f"Result: {num1 + num2}")
        elif option == 2:
            print(f"Result: {num1 - num2}")
        elif option == 3:
            print(f"Result: {num1 * num2}")
        elif option == 4:
            try:
                print(f"Result: {num1 / num2:.2f}")
            except ZeroDivisionError:
                print(f"Error: {num1} divided by {num2} will cause a ZeroDivisionError!")
        elif option == 5:
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
    except ValueError:
        print("ValueError! Option must be an integer.")