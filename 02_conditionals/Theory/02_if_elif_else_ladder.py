a = int(input("Enter your age: "))

if (a>18):
    print("You can drive.") # first, python check if condition.if it matches then it will print the given statement.



 # if 'if condition' does not matches then python will check elif.
elif (a==0):
    print("You are entering 0 which is not a valid age!")
# if it matches then python will print the given statement.



# if 'elif condition' does not matches then python will check next elif.
elif (a<0):
    print("You are entering invalid negative age!")
# if it matches then python will print the given statement.



# at last if no condition matches with input pyhon will print the statement which is given under else.
else:
    print("You are below the age of consent.\nYou can't drive.")



print("End 0f program")


# in if else elif ladder  
# python will follow that path only whose condtion matches first other wise ignore all (if and elif) and follow else path.