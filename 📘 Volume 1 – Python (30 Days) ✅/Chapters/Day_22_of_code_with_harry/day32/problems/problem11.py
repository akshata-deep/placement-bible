# Create:

# students_python = {"Akshata", "Anu", "Rahul", "Amruta"}
# students_sql = {"Akshata", "Rahul", "Kiran", "Sneha"}

# Find:

# Students studying either Python or SQL
# Students studying both
# Students studying Python but not SQL
# Students studying exactly one of the two

# Don't look for the answers. Solve each yourself.


students_python = {"Akshata", "Anu", "Rahul", "Amruta"}
students_sql = {"Akshata", "Rahul", "Kiran", "Sneha"}
print(students_python.symmetric_difference(students_sql))
print(students_python.intersection(students_sql))
print(students_python.difference(students_sql))