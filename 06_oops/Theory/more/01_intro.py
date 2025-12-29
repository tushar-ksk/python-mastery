class Car:
    # brand = None
    # model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"I have {self.brand} {self.model}."
    
    def fuel_type(self):
        return "petrol" or "desiel"

# inheritance
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_telsa = Electric_car("Tesla", "Model S", "85kwh")
# print(my_telsa.brand)
# print(my_telsa.model)
# print(my_telsa.battery_size)
# print(my_telsa.full_name())
print(my_telsa.fuel_type())



my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# my_new_car = Car("Ford", "Mustang")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())
