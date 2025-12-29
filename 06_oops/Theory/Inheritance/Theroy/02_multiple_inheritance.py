class Person():                                                          # Base class
    name = "Soham"
    def showname(self):
        print(f"Name of the Programmer is {self.name}.")
class Address(Person):                                                   # Derived class      (inheritance)
    address = "Bapoli"
    def showadd(self):
        print(f"{self.name} belongs to {self.address}")
class Coder():                                                           # Base class
    language = "Python"
    def showlang(self):
        print(f"Language used by Programmer is {self.language}")


class Programmer(Person,Coder):                                          # Derived class     (multiple inheritance) 
    company = "ITC Infotech"
    def showinfo(self):
        print(f"{self.name} uses {self.language} for coding in {self.company} company.")


'''Here Programmer is derived from both Person and Coder
where Person and Coder contains "different" attributes.                      >>>> This is called multiple inheritance
Therfore Programmer inherit properties of both Person and Coder.'''

a = Address()
a.showadd()

b = Programmer()
b.showinfo()
