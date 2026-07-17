a = "harry is very bad boy \nhello world "
print(a) #it will print in new line 

a = "harry is very bad boy \"hello world\""
# the " "must be printed as it is means we will do like this 
print(a) #it will print as it is in output but it will not put that \\ 

a = 'harry is very bad boy \'hello world\''
# the ' 'must be printed as it is means we will do like this 
print(a) #it will print as it is in output but it will not put that \\ 

# 1.\t -> tab
# 2.
a = 'harry is very bad boy \\hello world\\'
print(a)

a = 'it\'s raining'
print(a)

print("Hello\rHi") #Then \r moves back to the beginning, and "Hi" overwrites the first two

print("ABC\bD") # remove one char before it

print("Hello\fWorld")
print("Hello\vWorld")
print("\100") # print a char using its octal value 
# it will print "@" becouse the ocatl 100 reperests the symbol @
print("\101") # print a char using its octal value 
# it will print "A" becouse the ocatl 100 reperests the symbol A

print("\x41") #print the ASCII value