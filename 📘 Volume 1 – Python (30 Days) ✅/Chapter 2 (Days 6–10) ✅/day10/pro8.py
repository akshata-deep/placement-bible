# ========== SALARY SLIP ==========
# Employee Name :
# Basic Salary :
# Bonus :
# Gross Salary :
# Tax :
# Net Salary :

# Data Types
# Basic Salary :
# Bonus :
# Gross Salary :
# Tax :
# Net Salary :
# =================================



employee_name = "Akshata"
basic_salary = "55000"
bonus = "7500"
tax_percent = 10

basic_salary_int = int(basic_salary)
bonus_int = int(bonus)
gross_salary = basic_salary_int + bonus_int
tax_amount = (gross_salary * tax_percent) / 100
net_salary = gross_salary - tax_amount
print(f"========== SALARY SLIP ==========\n"
      f"Employee Name : {employee_name}\n"
      f"Basic Salary : {basic_salary}\n"
      f"Bonus : {bonus}\n"
      f"Gross Salary : {gross_salary}\n"
      f"Tax : {tax_amount}% \n"
      f"Net Salary : {net_salary}\n\n"
      f"Data Types :\n"
      f"Basic Salary : {type(basic_salary_int)}\n"
      f"Bonus : {type(bonus_int)}\n"
      f"Gross Salary : {type(gross_salary)}\n"
      f"Tax : {type(tax_amount)}\n"
      f"Net Salary : {type(net_salary)}\n"
      f"=================================")



print(int("12A"))