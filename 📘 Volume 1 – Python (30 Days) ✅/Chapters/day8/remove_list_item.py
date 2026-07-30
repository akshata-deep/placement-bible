# 1.POP() :it will just remove the end value in the list

l1 = [1,2,3,4,5]
l1.pop()
print(l1)
    # l1.pop(2:4) :we cant do this becouse it WILL ONLY REMOVE  one value 
    #  we can add index number in the pop function
l1.pop(3) # ---> this number is index
print(l1)

# 2.REMOVE : it will remove a specific item from the list 
l2 = [1,2,3,"hello",4,5]
l2.remove(1) #---> this is not a index it is value inside the list
l2.remove("hello") 
print(l2)

# 3.DELETE : it is strong then remove becouse it can delete One element,Multiple elements (using slicing),Even the entire list 

l3 = [1,2,3,4,5,6,7]
del l3[3]
del l3[1:3]
print(l3)
del l3
# print(l3) #it will show the error becouse del removed the list l3 only

#  4.CLEAR() : it will claer all the values in the list 

l4 = [1,2,3,4,5,6]
l4.clear()
print(l4) #---> empty []