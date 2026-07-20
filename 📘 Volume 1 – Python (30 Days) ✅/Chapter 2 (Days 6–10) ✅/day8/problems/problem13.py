# Write a program that:

# Asks the user to enter a fruit.
# If the fruit is present, print its first index.
# If the fruit is not in the list, print:


fruits = ["apple", "banana", "mango", "banana", "grapes"]
fruit = input("Enter the fruit :")
if fruit in fruits:
    couting = fruits.count(fruit)
    in_fruit = fruits.index(fruit)
    print(f"In list {fruit} is {couting} \n"
         f"first appereing index is :{in_fruit}")
    # print(couting)
else:
    print("Fruit not found!........")
