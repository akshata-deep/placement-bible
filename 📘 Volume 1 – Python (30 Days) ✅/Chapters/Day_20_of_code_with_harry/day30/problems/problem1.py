def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        answer = n*factorial(n-1)
        n -= 1
        return answer

n = int(input("Enter the number : "))
factorial = factorial(n)
print(f"The factorial of the {n} : {factorial}")