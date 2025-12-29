print("Sum of first N natural number.")

def total(n):
    if n== 0:
         return 0
    elif n<0:
        return "Number of terms cannot be negative!"
    elif n%1 != 0:
        return "Number of terms cannot be fractional!"
    else:
        return n+total(n-1)
       

n = float(input("Enter number of terms: "))
print(int(total(n)))