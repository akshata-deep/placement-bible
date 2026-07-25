# Q4. Divisible by 5 and 11

# Take an integer from the user.

# If divisible by both 5 and 11 → print "Divisible by both".
# Otherwise → print "Not divisible by both".

num = int(input("Enter the number :"))
if num %5 and num %11:
    print("this is diviseable by both 11 and 5 ")
else:
    print("not dvisble by both")