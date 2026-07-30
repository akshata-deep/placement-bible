########### REMAINDER :LIST IS MUTABLE #############






friend = ["apple","orange",5,345.06,False,"akshata","roshan"]
print(friend)


friend.append("Harry") #add the nnew valuse at the end of the list
print(friend)

numbers = [4,6,5,345.06,6,9,2,2]
numbers.sort()
print(numbers)


# numbers.reverse()
# print(numbers)

# numbers.insert(6,7) #numbers.insert(index, value) :at the 2 place add the 7 .....

# if we want to add two numbers
### METHOD 1 :

# numbers[1:6] = [2, 7] #IT WILL REPLACE ALL 1YO 6 NUMBERS WITH 2 AND 7
# print(numbers)

numbers.pop() #it will remove/delete the last number
print(numbers)

numbers.remove(6)# it will remove first 6 
print(numbers)

numbers.remove(2)
# numbers.remove(2)
print(numbers)
numbers.pop(3)
print(numbers) #it will remove index 3 element (it will remove 6 now)
