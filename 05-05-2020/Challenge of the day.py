def factorial(n):
    number = 1
    for i in range(1,n+1):
        number*=i
    return number
input = int(input("enter number larger than 1: "))
print(factorial(input), end= ',')
        