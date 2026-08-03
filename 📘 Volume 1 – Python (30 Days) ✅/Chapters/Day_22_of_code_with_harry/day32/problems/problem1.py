# s1 = {1, 2, 3}
# s2 = {3, 4, 1}
# # print(s1.union(s2))
# # print(s1.intersection(s2)) 

# s1.update(s2)
# print(s1, s2) #s1 = {1, 2, 3, 4} s2 = {3, 4, 1}
# s1.intersection_update(s2)
# print(s1) #s1 = {1, 3, 4}



# s1 = {1, 2, 4, 5}
# s2 = {1, 2, 6, 8}
# s1.intersection_update(s2)
# print(s1)


s1 = {1, 2, 3, 4}
s2 = {4, 1, 6}
# print(s1.symmetric_difference(s2))

print(s1.difference(s2))
print(s2.difference(s1))
# s1.isdisjoint_update(s2) #this keyword is not in the python
print(s1.isdisjoint(s2))

print(s1.issuperset(s2))
print(s2.issubset(s1))

s1.remove(3)
print(s1)

s1.clear()
print(s1)