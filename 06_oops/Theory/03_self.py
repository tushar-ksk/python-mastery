class employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} is language and the salary is {self.salary}.")

    def greet(self):
        print(f"good morning {self.name}")


rohan = employee()
# (rohan.getInfo()) = employee.getinfo(rohan)
rohan.getInfo()
rohan.name = "Rohan"
rohan.greet()