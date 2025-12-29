# Poly - multi     morphism - forms
# Polymorphism means existance of an method in multiple forms

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
print(my_telsa.fuel_type())

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())