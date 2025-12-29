name = input("Enter Username: ")
if len(name)<10 or len(name)>20:
    print("Username must contain 8-20 characters!")
else:
    print("Hey",name,"\nHow are you?")