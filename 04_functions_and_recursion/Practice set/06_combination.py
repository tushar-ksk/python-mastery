# Factorial

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n* factorial(n-1)

# Combination

def combination(n,r):
    if n>=r:
        return (factorial(n)/((factorial(n-r))*factorial(r)))
    else:
        return "r cannot be greator than n"

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

print(int(combination(n,r)))