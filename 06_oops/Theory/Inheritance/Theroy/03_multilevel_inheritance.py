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


class Programmer(Address,Coder):                                          # Derived class     (multiple inheritance) 
    company = "ITC Infotech"
    def showinfo(self):
        print(f"{self.name} lives in {self.address} and uses {self.language} for coding in {self.company} company.")


'''Here Adress is derived from Person 
and Programmer is derived from Address not from Person                        >>>> This is called MUltilevel Inheritance
but indirectly Programmer contains 
properties/attributes of both Address and Person.'''


a = Address()
a.showadd()

b = Programmer()
b.showinfo()