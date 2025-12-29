print("Factorial Calculator !")

n = int(input("Enter the number: "))
f = 1
i=1
while i<= n:
    f*=i
    i+=1
print(f"{n}! = {f}")




print("Factorial Calculator !")

n = int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f *= i
print(f)