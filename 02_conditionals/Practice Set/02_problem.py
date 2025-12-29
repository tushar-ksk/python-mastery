# pass fail test

a = input("Enter Your Name: ")
b = int(input("Enter Your ENGLISH Marks(Out of 100): "))
c = int(input("Enter Your HINDI Marks(Out of 100): "))
d = int(input("Enter Your MATHS Marks(Out of 100): "))

if (b>33 and c>33 and d>33):
    if (((b+c+d)/3)>40):
     print(a,"passed the exam.")
   
else:
   print(a,"failed in exam.")




# pass fail test
# better

a = input("Enter Your Name: ")
b = int(input("Enter Your ENGLISH Marks(Out of 100): "))
if b > 33:
    c = int(input("Enter Your HINDI Marks(Out of 100): "))
    if c > 33:
        d = int(input("Enter Your MATHS Marks(Out of 100): "))
        if d > 33:
            if (((b+c+d)/3)>85):
                print(a,"is in merit list.")
            elif (((b+c+d)/3)>33):
                print(a,"passed the exam.")

else:
     print(a,"failed in exam.") 