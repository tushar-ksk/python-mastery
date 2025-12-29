print("Fahrenhite to Celsius")
def f_to_c(f):
    c = (5/9)*(f-32)
    return round(c,2) # round is an inbuilt python function which round first argument upto second argment 

f = float(input("Enter Temprature In Fahrenhite: "))

print(f"Given Temprature is {f_to_c(f)}°C")