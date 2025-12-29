def func():
    print("This is a function in module.")
    return "Function executed successfully."

# func()

# print("")

# print(func())

print(__name__)            
print(func.__name__)

# print(func.__module__)

# # print(func.__doc__)

# if __name__ == "__main__":
#     print("we are directly running this code")