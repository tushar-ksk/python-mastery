a= float(input("Enter your first number:", ))
b= float(input("Enter your second number:", ))
print("Press A for addition\nPress S for subtration\nPress M for multiplication\nPress D for division\n")
d=input("Enter the operation to be applied : ").upper()

if d== "A":
    print("You chose",a,"+",b)
    print("which is equal to",a+b)
elif d== "S":
    print("You chose",a,"-",b)
    print("which is equal to",a-b)
elif d== "M":
    print("You chose",a,"*",b)
    print("which is equal to",a*b)
elif d== "D":
    print("You chose",a,"/",b)
    print("which is equal to",a/b)
else:
    print("unvalid operation 😵‍💫")