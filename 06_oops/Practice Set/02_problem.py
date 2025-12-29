# calculator class for sqr cube sqrt of a number
print("")
class calc:

    def sqr(self):
        
        a = float(input("Enter your number for finding square >>> "))
        print(f"Square of {a} is {a**2}")

    def cube(self):

        b = float(input("Enter your number for finding cube >>> "))
        print(f"Cube of {b} is {b**3}")

    def sqrt(self):

        c = float(input("Enter your number for finding square root >>> "))
        print(f"Squre root of {c} is {c**0.5}")

    @staticmethod
    def hello():
        print("Hello there..")

num = calc()
num.hello()
num.sqr()
num.cube()
num.sqrt()
print("")