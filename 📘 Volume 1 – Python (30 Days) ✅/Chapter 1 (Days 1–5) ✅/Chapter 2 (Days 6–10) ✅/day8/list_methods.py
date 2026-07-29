# # 1.SORTING

# colors = ["violet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# print(num)


#             # IF WE WNAT TO REVERS THE SORTED ELEMENT (DECREACTING ORDER) :reverse=Ture

# colors = ["violet", "indigo", "blue", "green"]
# colors.sort(reverse=True)
# print(colors)
#             # we can use like both
# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.sort()
# num.reverse()
# print(num)

# # 2.reverse()
# colors = ["violet", "indigo", "blue", "green"]
# colors.reverse() #it will just revers the list
# print(colors)

# num = [4,2,5,3,6,1,2,1,2,8,9,7]
# num.reverse()
# print(num)


# # 3.index()

# colors = ["violet", "green", "indigo", "blue", "green"]
# print(colors.index("green")) #we know the name but we what index number menas use this

# num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
# print(num.index(3)) #we know the index number but we what in that index what data is there means use this 



# # 4.count

colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))


# 5.copy():


colors = ["red", "blue","akshata","hello","anu"]

newlist = colors 
            # in this case what happens means it will store same value toboth but we made a new operation in just newlist in upcomeing line it will also make chnage in color (BASICALLY WHAT EVER CHANGE YOU DO THEY WILL STORE IN BOTH)

newlist.sort()
print(newlist)
print(colors)

            # TO OVERCOME THIS WE USE COPY()

colors = ["violet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)
newlist.sort()
print(newlist)
print(colors)


