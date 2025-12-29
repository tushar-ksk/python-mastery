class num:
    a = 1

    def show(self):
        print(f"The class attribute is {self.a}")

n = num()
n.a = 45    #instance attribute
n.show()



class num:
    a = 1
    @classmethod
    def show(self):
        print(f"The class attribute is {self.a}")

n = num()
n.a = 45
n.show()