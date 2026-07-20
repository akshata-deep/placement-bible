# append() :it will add at the end of the list

l1 = [1,2,6,4,3,6,7]
l1.append(10)
print(l1)

# 1.sort() :it will sort in increasing order

l1.sort()
print(l1)


# 2.insert() : at the specific position we can insert the value
# rimember: we must use , between the valuesin insert function

l1.insert(3,"Hello")
print(l1)

# 3.extand() : here what will do for exacting list only we add other list we will not make other list and put this both list values

l2 = ["hello","hi",10,40]
l1.extend(l2)
print(l1) #you can see here li and l2 values and in l1 itself we just puted the l2 in l1

# 3.concatination : here we add to list and store i new list

l3 = l1 + l2
l3.sort()
print(l3)


