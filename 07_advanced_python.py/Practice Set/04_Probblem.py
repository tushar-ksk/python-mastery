a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))

try:
    result = a / b
    print(f"{a}/{b} = {round(result,3)}")

except ZeroDivisionError as z:
    print(f"Error: {z} - Division by zero is not allowed.")
    print("You will get ∞ ∀ numberators")
