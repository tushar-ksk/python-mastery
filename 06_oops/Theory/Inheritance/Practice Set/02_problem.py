class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    
    @staticmethod
    def bark():
        print("BHOW! BHOW!")


d = Dogs()
d.bark()
