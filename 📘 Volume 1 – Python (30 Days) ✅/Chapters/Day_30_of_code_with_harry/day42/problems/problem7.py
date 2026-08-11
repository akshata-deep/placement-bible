# Create a program that prints a numbered menu using enumerate().

menu = ["Add", "Subtraction", "Multiplication", "Division", "Exit"]

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")