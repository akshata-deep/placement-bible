# Handle ZeroDivisionError and print "Calculator Closed" using finally.

try:
    print(10/0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Calculator Closed !")