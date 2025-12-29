# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand
    @staticmethod
    def car_description():
        return "Cars are not only means of transport but also they are good friend."

tesla = Car("Telsa", "CyberTruck")

# print(tesla.__brand)  it is private method therefore it will not run
print(tesla.get_brand())
print(tesla.car_description())