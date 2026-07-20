# Using list comprehension, create a new list that contains only the numbers greater than 10.

numbers = [5, 12, 3, 18, 7, 20, 1]
greater = [num for num in numbers if num >10]
print(greater)