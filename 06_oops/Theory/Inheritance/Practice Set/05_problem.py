class Vector:
    
    def __init__(self,i=0,j=0,k=0):
        self.i = i
        self.j = j
        self.k = k

    def showvector(self):
        sign1 = '+' if self.j > 0  else '-'
        sign2 = '+' if self.k > 0  else '-'
        return f"{self.i}i {sign1} {abs(self.j)}j {sign2} {abs(self.k)}k"

    def __str__(self):
        sign1 = '+' if self.j > 0  else '-'
        sign2 = '+' if self.k > 0  else '-'
        return f"The resultant vector is: {self.i}i {sign1} {abs(self.j)}j {sign2} {abs(self.k)}k"
    
    def __add__(self,v2):
        return Vector(self.i+v2.i,self.j+v2.j,self.k+v2.k)
    
    def __mul__(self,v2):
        return self.i*v2.i+self.j*v2.j+self.k*v2.k
    
    def __rmul__(self, scalar):
        return Vector(scalar * self.i, scalar * self.j, scalar * self.k)
    

v1 = Vector(2,3,4)
v2 = Vector(1,-2,3)
v = v1 + v2
print(v)
print(v.showvector())

print(v1*v2)
print(3*v1)
