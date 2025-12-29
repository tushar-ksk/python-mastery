'''
for n = 3
  *
 ***
*****
'''

n = int(input("enter your number: "))
for i in range(1,n+1):
    print(" "*(n-i), end ="")
    print("*"*(2*(i)-1))

n = int(input("enter your number: "))
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*(i)-1))
