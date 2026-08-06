# Ask the user for a filename (simulate with input), handle errors, and print "File Closed" using finally.


try:
    filename = input("Enter the filename :")
except:
    print("Error")
finally:
    print("File Closed")