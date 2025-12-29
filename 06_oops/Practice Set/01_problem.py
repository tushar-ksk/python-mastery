# create a class programmer for storing information of few programmers working Microsoft

class Programmers:
    job = "Programmer"
    company = "Microsoft"

    def __init__(self, name, salary, address):

        self.name = name
        self.salary = salary
        self.address = address
    
    def showinfo(self):
        print(f"{self.name} lives in {self.address} and work as {self.job} in {self.company}, earning ${self.salary} per annum.")
        print("")

while True:

    e = input("Press \"enter\" if you want to fill your details \nor Press any \"other key\" and then \"enter\" if you want to exit ")
    print("")
    if e == "":
        name = input("Enter your name >>> ")
        salary =  int(input("Enter your salary >>> "))
        address = input("Enter your address >>> ")

        p = Programmers(name, salary , address)
        p.showinfo() 
        print("Thanks....")

    else:
        print("program exhausts....")
        print("")
        break
