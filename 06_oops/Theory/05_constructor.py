class person:
    lang = "Python"
    salary = 1200000

    def __init__(self): # dunder method which is automatically called
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.lang} and the salary is {self.salary}.")

ramfal = person()
ramfal.name = "Ramfal"
ramfal.getInfo()