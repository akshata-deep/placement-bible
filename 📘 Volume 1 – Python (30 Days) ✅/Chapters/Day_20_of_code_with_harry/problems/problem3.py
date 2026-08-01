# Q3 — Medium

# Create a function:

# calculate_area(length, width)

# Add a docstring explaining what the function does.

# Call the function and print its result.

# Then print its docstring.



def calculate_area(length, width):
    "By takeing the length and width as input inside the main fuction and fuction will calculte the area and return area "
    area = length * width
    return area





length = int(input("Enter the length : "))
width = int(input("Enter the width : "))
print(calculate_area(length,width))
print(calculate_area.__doc__)
