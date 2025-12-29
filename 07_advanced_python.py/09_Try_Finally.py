# try:
#     a = int(input("Enter a number: "))
#     print("The number is:", a)

# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# finally:
#     print("This block will always execute, regardless of exceptions.")

# # use of finally block comes in function here we can use simple print statement

# print("This block will always execute, regardless of exceptions.")




def divide_numbers():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = a / b
        print("The result is:", result)
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return ("Error: Division by zero is not allowed.")
    
    finally:
        print("This block will always execute, regardless of exceptions.")
    print("This block will always execute, regardless of exceptions.")       # this will not execute because return statement is used before this print statement
#     # finally block will always execute


print(divide_numbers())


#  the finally statement will always executes before the function returns the value but if we put print statement in finally block it will execute first and then return the value from function