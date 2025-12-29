print("")

try:    
    a= int(input("Hey, enter a number: "))
    print("")
    print("You entered:", a)

# except ValueError as v:
#     print(f'''That's not a valid number!
# {v}''')



except Exception as e:
    print(f'''That's not a valid number!
{e}''')
print("")
print("End of program")
print("")