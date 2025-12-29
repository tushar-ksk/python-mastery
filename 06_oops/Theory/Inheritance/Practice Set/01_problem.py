class TwoDvector():
    i = ""
    j = ""

    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
class ThreeDvector(TwoDvector):
    k = ""

    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvector(2,3)
b = ThreeDvector(5,9,5)
a.show()
b.show()


