# global a     # writing global variable outside the function will not effect value of a inside the function when a is defined inside the function, but outside the function no matters if we write global or not

a = 5

def show():
    global a  # when we write global a inside the function, it means we are using the global variable a
    # if we don't use global a, it will create a new local variable a inside the function

    a = 45  # this line changes the global variable a to 45
   
    print(a)

print(a) # print statement before calling the function will print 5 
show()
print(a) # print statement after calling the function will print 45 because we changed the global variable a to 45 inside the function