l = ["Tushar","Soham","sharma","Satyam","Rohan"]


for name in l:
    if name[0].upper()== "S":
        print(name)



l = ["Tushar","Soham","sharma","Satyam","Rohan"]

for name in l:
    if (name.upper()).startswith("S"):
        print(f"Hello {name}")