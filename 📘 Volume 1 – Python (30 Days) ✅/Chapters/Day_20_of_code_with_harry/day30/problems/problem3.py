def recursive(n):
    if n == 1:
        return 1
    else:
        print(n)
        recursive(n-1)

n = int(input("Enter the number : "))
recursive(n)