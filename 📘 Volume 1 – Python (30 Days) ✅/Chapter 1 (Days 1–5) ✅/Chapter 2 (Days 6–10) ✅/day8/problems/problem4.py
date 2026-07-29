# Create a new list that:

# Keeps only even numbers, and
# Multiplies each even number by 10.



numbers = [1, 2, 3, 4, 5, 6]
even_num = [num*10 for num in numbers if num%2==0 ]
print(even_num)