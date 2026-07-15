


Fahrenheit = float(input("enter the Fahrenheit :"))
Celsius = float(input("enter the Celsius :"))
Kelvin = float(input("enter the Kelvin :"))
what = (input("which you want : "))

if what == "Celsius to Fahrenheit" :
    Fahrenheit = (Celsius * 9/5) + 32
    print("Celsius → Fahrenheit :", Fahrenheit)
elif what == "Fahrenheit to Celsius" :
    Celsius = (Fahrenheit - 32) * 5/9
    print("Fahrenheit → Celsius :", Fahrenheit)
elif what == "Celsius to Kelvin" :
    Kelvin = Celsius + 273.15
    print("Celsius → Kelvin :", Kelvin)
elif what == "Kelvin to Celsius" :
    Celsius = Kelvin - 273.15
    print("Celsius → Kelvin :", Celsius)
elif what == "Fahrenheit to Kelvin" :
    Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
    print("Fahrenheit → Kelvin :", Kelvin)
elif what == "Kelvin to Fahrenheit" : 
    Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
    print("Kelvin → Fahrenheit :", Kelvin)
else :
    print("give me correct like for example : Kelvin to Fahrenheit \n dont warry try again")