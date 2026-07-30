



def montly_salary(basic_salary,bouns = 3000):
    total_salary = basic_salary + bouns
    return total_salary


print("---------------------------------------")
basic_salary = int(input("Enter your salary :"))
this_month_salary = montly_salary(basic_salary)
print(f"YOUR THIS MONTH SALARY IS :{this_month_salary}\n"
      f"---------------------------------------")
