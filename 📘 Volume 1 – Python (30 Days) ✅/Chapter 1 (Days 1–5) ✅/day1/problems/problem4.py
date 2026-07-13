# write a python program to print the contrnts of a directory using the OS module search online for the function which does that

import os

# Specify the directory path
path = "problems"      # "." means the current directory

# Get the list of files and folders
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)


    # The os module is a built-in Python module that lets your Python program communicate with the Operating System (OS)

    # this program shows the files whichfiles are there in the folder