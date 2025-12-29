class Number:
    def __init__(self,n):
        self.n = n

    def __sub__(self,num):
        return Number(self.n - num.n)
    
    def __str__(self):
        return str(self.n)

a = Number(1)
b = Number(2)
c = Number(8)
print(c-b-a)
