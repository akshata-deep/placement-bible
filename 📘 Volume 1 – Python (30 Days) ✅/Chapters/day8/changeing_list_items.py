# LIST ARE MUTABLE MEANS WE CAN CHNAGE AFTER CREATEING IT 

names1 = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names1[2] = "Akshata","hello" 
    #remember : this will store as a tuple inside the list
names1[2] = "Akshata","akshata" 
print(names1)


names2 = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
print(names2)
names2[2:4] = "akshata","hello"
print(names2)


# What if the range of the index is more than the list of items provided?

names3 = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names3[1:3] = "akshata", "hello","sfsd","fsff", "sffd"
#if we add more values means it will make a space for them
print(names3)
names3[1:5] = "badhsad", "bsbfds" #in this  case it will delete ""sfsd","fsff""
#if we add less values means it will detele other values 
print(names3)



