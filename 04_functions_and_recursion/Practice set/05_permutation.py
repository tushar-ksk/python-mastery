# Factorial

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n* factorial(n-1)

# Permutation

def permutation(n,r):
    if n>=r:
        return factorial(n)/(factorial(n-r))
    else:
        return "r cannot be greator than n"


i=1

while i>0:

  n = int(input("Enter the given number of Items: "))
  r = int(input("Enter the number of items to be arranged: "))

  print(f"There are {int(permutation(n,r))} number of ways to arrange them.")