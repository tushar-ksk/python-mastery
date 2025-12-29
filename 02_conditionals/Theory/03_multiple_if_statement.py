a = int(input("Enter your favourite number: "))



# if statement no.1
    
if (a%2==0):
    print("it is an even number")


    #conditions under condition
     
    if (a%3==0):
        print("it is an multiple of 6")
        
    else:
        print("it is not a multiple of 6")
        
        
# end of if statement no.1


# if statement no.2

if (a%(2 or 3 or 5 or 7)):
    print("it is an prime number.")

else:
    print("it is not a prime number")

# end of if statement no.2


print("End of program")