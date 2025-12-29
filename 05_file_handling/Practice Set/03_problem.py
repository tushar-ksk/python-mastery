
def generateTables(n):

    a = ""

    for i in range(1,11):
        a+= f"{n}X{i} = {n*i}\n"

        with open(f"Tables/Table of {n}","w") as t :
            t.write(a)

        
for i in range(2,21):
    generateTables(i)
            