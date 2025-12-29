# #PROBLEM 1
name = input("Enter your name: ")
print("Good Afternoon", name)
print(f"Good Afternoon {name}")     # this is f string (new feature of python)



# PROBLEM 2
letter= '''Dear <|Name|>,
                You  are selected!
                <|Date|>'''

Name = input("Enter Your Name: ")
Date = input("Enter Date: " )
print("required letter is :")
print(letter.replace("Name",Name).replace("Date",Date))



# #PROBLEM 3
str1 = "Tushar is a good  boy and"

print(str1.find("  "))              #find will report index no. when it find substringand -1 when it doesn't find double space.




# #PROBLEM 4 
str1 = "Tushar is a good boy and\nhe is not a  bad boy"

print(str1.replace("good",""))
print(str1)                         #strings are immutable which means that you cannot change them by running functions on them




#PROBLAM 5
letter = "Dear Tushar, this python practice set is nice. Thanks!"
print(letter)
letter2 = "Dear Tushar,\n\tThis python practice set is nice.\nThanks!"
print(letter2)