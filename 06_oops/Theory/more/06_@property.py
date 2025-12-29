# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model
    
    @property
    def model(self):
        return self._model   # getter
    
    @model.setter
    def model(self,model):
        self._model = f"Tesla {model}"  # setter


#before using setter

tesla = Car("Telsa", "CyberTruck")
print(tesla.model) # we have made model attribute private but we have also defined a method as model that's why it executes successfully.
# tesla.model = "S" # we can't do this as we didn't use setter till now. 


# after using setter

tesla.model = "S"
print(tesla.model)


# isinstance is used to check whether a object in is instance of a class.
print(isinstance(tesla,Car))
