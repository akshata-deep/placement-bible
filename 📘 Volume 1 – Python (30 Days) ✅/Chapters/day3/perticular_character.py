# REMEMEBER : -> harry {0,1,2,3,4}
#            : <- harry {-5 , -4 , -3 , -2 , -1}


# to pint a perticular cahr in the string means we wnat to use this 

# a = name [ind_start:ind_end]

# example :
a = "harry"
b = a[0:3]
print(b) # output will be this :har (it will count only 0,1,2 -> not 3)

a = "harry"
b = a[-4:-1]
print(b) # output will be this :arr (it will count only -3, -2, -1 -> not -4)


# if we wnat to print a perticular char in the string means use this 

a = "harry"
character1 = a[1]
print(character1) # output will be a 

a = "harry"
character2 = a[-2]
print(character2)  # output will be r
