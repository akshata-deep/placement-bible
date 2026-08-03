# Create two sets and modify the first set so that it contains only common elements.



a = {1, 2, 3, 4}
b = {4, 5, 6}
a.intersection_update(b)
print(a)