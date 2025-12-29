print("")
a = int(input("Hey, enter a number: "))
b = int(input("Hey, enter another number: "))

if b==0:
    raise ZeroDivisionError("You can't divide by zero!")
else:
    print(f"{a} / {b} = {a/b}")
print("")


# this will crash the program 

# but when we use try/except, we can handle the error and continue the program