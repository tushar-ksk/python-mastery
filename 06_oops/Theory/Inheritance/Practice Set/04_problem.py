class Complex:

    def __init__(self, r = 0 , i = 0):
        self.r = r 
        self.i = i

    def shownum(self):
        return self.__str__()

    def __str__(self):
        if self.r == 0 and self.i == 0:
            return "0"
        elif self.r == 0:
            return f"{self.i}i"
        elif self.i == 0:
            return f"{self.r}"
        else:
            sign = '+' if self.i > 0 else '-'
            return f"{self.r} {sign} {abs(self.i)}i"

    def __add__(self, c):
        return Complex(self.r + c.r, self.i + c.i)
    
    def __mul__(self, d):
        real = self.r * d.r - self.i * d.i
        img = self.i * d.r + self.r * d.i
        return Complex(real, img)

c1 = Complex(2, 5)
c2 = Complex(0)
c3 = Complex(3)
c4 = Complex(0, 0)

print("c1:", c1)    # 2 + 5i
print("c2:", c2)    # 3i
print("c3:", c3)    # 3
print("c4:", c4)    # 0

a = c1 + c2
print("c1 + c2:", a)  # 2 + 8i

m = c1 * c2
print("c1 * c2:", m)  # -15 + 6i


# Example usage
c1 = Complex(2, 5)
c2 = Complex(3,0)

print(c1.shownum())     # 2 + 5i
print(c2.shownum())     # 3

a = c1 + c2
print(a)                # 5 + 5i
print(a.shownum())      # 5 + 5i

m = c1 * c2
print(m)                # 6 + 15i
print(m.shownum())      # 6 + 15i
