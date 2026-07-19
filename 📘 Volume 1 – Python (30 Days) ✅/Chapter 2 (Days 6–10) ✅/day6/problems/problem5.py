# SI = (Principal × Rate × Time) / 100

def intrest(Principal,Rate,Time):
    SI = (Principal * Rate * Time) / 100
    return SI

Principal = int(input("enter the Principal :"))
Rate = int(input("enter the Rate :"))
Time = int(input("enter the Time :"))
print(intrest(Principal,Rate,Time))