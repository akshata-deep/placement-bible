############ tuple is immutable (we cant change) ######### 

# diffrences  list            tuple
#               []              ()
#           mutable           immutable

# what if i want to add only one elment in the tuple 
a = (1)
print(type(a)) # it will not store as a tuple it will show you as type of that variavle but as a int

# # so to do the one element tuple you wnat to add this small commom after the fisrt element 
# b = (1,)
# print(type(b)) #it will store as the tuple


########### OPERATIONS


# 1.REPEAT
a = (1,4,6,5)
print(a*5)

# 2.CONCATINATION
f = (2,5,3,2)
g = (3,4,2,4)
print(f+g)

# 3.CHECKING THE VALUSE
print(3 in f) # 3 is there in the tuple means it will return as Ture
print(7 in f) # 7 is there is not in the tuple means it will return as False

# 4.lenth
print(len(f))

#5.sliceing
sliced = a[1:3]
print(sliced) #it will give me new tuple
print(a) #but the original tuple will be as it is

# 6. unpacking
student = ("akshata",7,"a-div")
# if we wnat to assign the tuple valuse to assign in different to use in the symple 
name,usn,div = student
print(name,div)