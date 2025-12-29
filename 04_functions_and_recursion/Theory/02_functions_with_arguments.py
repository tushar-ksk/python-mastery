def goodDay(name, ending= "Thank you"): # if we donot give value of ending in function call then it will automatically take value from here. 
    print("GOOD DAY",name)
    print(ending)
    return "Done."

a= goodDay("Tushar","Thank You")
print(a)
goodDay("Soham")
goodDay("Satyam")
b= goodDay("Mannat", "Thanks")
print(b)