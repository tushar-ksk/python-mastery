class info:
  # class attributes
    language = "Python"
    salary = 1200000
    address = "Haryana"



soham = info()
# all areinstance or object attributes
soham.name = "Soham"
soham.sername = "Sharma"
print(soham.name, soham.sername)



tushar = info()
# name is instance attribute but language is class attribute 
tushar.name = "Tushar"
print(tushar.name,tushar.language)



rohan = info()
rohan.name = "Rohan" # instance attribute
rohan.salary = 65000 # since value of salary is changed therefore it become instance attribute
print(f"{rohan.name} earns {rohan.salary} per month")




# Note : instance attribute take prefrence over class attribute.