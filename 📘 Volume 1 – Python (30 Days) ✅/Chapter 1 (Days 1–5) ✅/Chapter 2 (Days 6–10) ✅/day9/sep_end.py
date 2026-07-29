print("hey i am ",4,7,4,sep="^")
# it will separate every words by that ^ character
# you can guive any charater



print("hey i am ",4,7,4,end=" ")
# it will just add that in end 
# in this cae the print fuction will not use \n

# print("Hello")
# print("World")

# Internally becomes:

# print("Hello", end="\n")
# print("World", end="\n")

# Output:

# Hello
# World

# but when we did this

# print("hey i am ", 4, 7, 4, end=" hey i am end")

# it will skip /n and direct print next line 


print("hello \\nworld")