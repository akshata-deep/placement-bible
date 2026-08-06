# Ask the user for an index of a list. Handle invalid indexes using except, and print "Program Finished" using finally.


try:
    print([1,2,3,4,][10])
except:
    print("indexError")
finally:
    print("Finally")