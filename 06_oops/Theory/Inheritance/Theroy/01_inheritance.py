# Inheritance is a way of creating a new class from an existing class.

class person:
    name = "tushar"
    country = "india"
    
class goodperson:
    name = "tushar"
    country = "india"
    hobby = "reading books"
    

a = person()
print(a.name,a.country,)

b = goodperson()
print(b.name,b.country,b.hobby)

''' Same task can be done in more efficient way as written below:
Also if we make say 10 class which contain some common attribute and if 
want to change them, we don't have to change them one by one. If we just 
make change in base class then it will automatically done in other derived class'''


class banda:              # Base class
    naam = "Tushar"
    gaam = "Didwara"

class badhiya(banda):     # Derived class or child class  
    hobby = "reading books"


a = badhiya()
print(a.naam,a.gaam,a.hobby)