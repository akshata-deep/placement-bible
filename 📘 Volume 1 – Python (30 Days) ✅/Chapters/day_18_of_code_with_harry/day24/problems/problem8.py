# 8. Deadly High – Tuple Demonstration

# Question:

# Create the tuple:

# products = ("Laptop", "Mouse", "Keyboard", "Monitor", "Printer")

# Perform the following:

# Print the complete tuple.
# Print the length.
# Check whether "Mouse" exists.
# Create another tuple containing only the last three products using slicing.
# Print the new tuple.
# Try changing the first element (observe the error).
# Comment (#) why the error occurs.


products = ("Laptop", "Mouse", "Keyboard", "Monitor", "Printer")



print(products)
print(len(products))
if "Mouse" in products:
    print("found")
else:
    print("not found ")
new_tuple = products[-3:]
print(new_tuple)
new_tuple.insert(20,2)#AttributeError: 'tuple' object has no attribute 'insert'