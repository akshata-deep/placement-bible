def recursive(n):
    if n == 1:
        print(n)
    else:
        print(n)
        recursive(n-1)

n = int(input("Enter the number : "))
recursive(n)