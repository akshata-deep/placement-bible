# Modify the ATM program to allow only withdrawals that are multiples of 100.


year = int(input("Enter the year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")