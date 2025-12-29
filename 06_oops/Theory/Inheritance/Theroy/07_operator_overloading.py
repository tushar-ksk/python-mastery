class Number:
    def __init__(self,n):
        self.n = n

    def __sub__(self,num):
        return self.n - num.n


a =  Number(1)
b = Number(2)

print(b-a)


class Number:
    def __init__(self,n):
        self.n = n

    def __sub__(self,num):
        return self.n + num.n    # here we change the meaning of + in class Number


a =  Number(1)
b = Number(2)
print(b-a)