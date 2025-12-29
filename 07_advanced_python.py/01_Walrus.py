# Aam Zindgi
# >> phle variable ko define kiya fir use if statement mein use kiya

list = [1,2,3,4,5]
n = len(list)
if n > 3:
    print(f"List is too long ({n} elemets, expected <=3)")


# Walrus Zindgi
# >> if statement mein hi variable ko define kar diya

if (n:= len([1,2,3,4,5])) >3:
    print(f"List is too long ({n} elemets, expected <=3)")
