# in function 

# spam detector

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click here"

message = input("Enter Your Comment: ").lower() # lower() convert entered message in lower case so that spam comments match with above phrases if written in mixed lower and upper case.

if p1 in message or p2 in message or p3 in message or p4 in message :
    print("This comment is a spam ")

else:
    print("this comment is not a spam")