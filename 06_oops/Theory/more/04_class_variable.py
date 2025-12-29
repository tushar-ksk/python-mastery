
class Car:
    
    total_cars = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars +=1
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

print(Car.total_cars) # class variable or attribute it associate with the entire class and all objects.