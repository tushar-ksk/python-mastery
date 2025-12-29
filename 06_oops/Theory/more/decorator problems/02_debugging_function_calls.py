
def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(str(kwarg) for kwarg in kwargs)
        print(f"Calling {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        
        return func(*args,**kwargs)
    
    return wrapper




@debug
def greet(name, sername, greeting="Hello"):
    print(f"{greeting}, {name} {sername}")

greet("Tushar", sername = "Sharma")

