a= input("Enter your first number: ") # a=1
b= input("Enter your second number: ") #b=2
print("Your first number is",a)
print("Your second number is",b)
print("sum is",a+b)                     # this will give output as "sum is 12"
# because by default it take input as string hence to apply operations on numbers we will use typcasting for input function


a = int(input("Enter your first number: "))  # a=1
b = int(input("Enter your second number: ")) #b=2

print("Your first number is",a)
print("Your second number is",b)
print("sum is",a+b)                         # now we get "sum is 3"


print("reminder when",a,"is divided by",b, "is", a % b)

c = int(input("enter first number:", ))
d = int(input("enter second number:", ))
print("c is greater than or equal to d is", c >= d)


c = int(input("enter number one: ", ))
d = int(input("enter numebr two: ", ))
print("mean of given two numbers is", (c+d)/2)


a = float(input("enter your number",))
''' print(a^2) this will not give result
we have to use print(a**2)'''
print("square of the given number number is",a**2)