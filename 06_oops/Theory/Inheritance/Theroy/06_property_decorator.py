class Employee:
    a = 1
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.name = "Tushar Sharma"
print(e.name)
print(e.fname)
print(e.lname)
print(e.fname,e.lname)