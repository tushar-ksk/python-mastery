list = [2, "Tushar", False, 45, "rohan"]

i=0

while (i<len(list)): # jab jab i ki value list ki length se choti ho toh
    print(list[i])   # list me jis item ka index number i ke equal hai vo print karo
    i+=1             # i ki exisiting value mein 1 jod ke use i ke sath assign kardoi = 1 # why we take i=0 not i=0 as we take 



tuple=(1, 3, 54, 43, 64)

i=0

while i<len(tuple):
    print(tuple[i])
    i+=1




dict= {
    1: "Tushar",
    2: "Soham",
    3: "rohan",
    4: "mohan",
    5: "rohit",
    6: "kirmada"
}

i=1 
# why we take i= 1 not i= 0 as we have taken in case of tuple and list?
# Ans:- because her i doesn't represent index number as it represent in tuple and lists but it represent key and in our dictionary key is started from 1.
while (i<len(dict)+1): # why we are using i<len(dict)+1 here but we have used i<len(tuple) or i<len(list) in above cases?
                       # Ans:- Because in above cases of tuple and lists i represents index number and here i represents key therefore last key is 6 and len(dict)=6 if we use i<len(list) it will stop at 6 and does not print the value at i=6, so we use i<len(dict)=1 that means 6+1=7 therefore loop will terminate at i=7 and last printed value will be value of 6.
    print(dict[i])
    i +=1