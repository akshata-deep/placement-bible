# 5. Star Pattern

num = int(input("Enter the number of lines : "))
if num <= 0 :
    print("------------")
else :
    for i in range (1,num+1) :
        for j in range(1,i+1) :
            print("*" , end = " ")
        print("\n")

# end = " " : this is actually tell the dont go to the next line or dont print anything 
# "" : did this menas it will not print anything
# " " : if there is space between also it will print as it is 