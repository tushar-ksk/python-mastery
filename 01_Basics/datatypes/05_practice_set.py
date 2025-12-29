# # PROBLEM1

fruits =[]

f1 = input("Enter fruit name: ")
f2 = input("Enter fruit name: ")
f3 = input("Enter fruit name: ")
f4 = input("Enter fruit name: ")
f5 = input("Enter fruit name: ")
f6 = input("Enter fruit name: ")
f7 = input("Enter fruit name: ")
f = [f1,f2,f3,f4,f5,f6,f7]
fruits.extend(f)
print("here is the list of fruits you chose :\n",fruits)




# PROBLEM2 
# increasing order
marks =[]
m1 = int(input("Enter Your Marks: "))
m2 = int(input("Enter Your Marks: "))
m3 = int(input("Enter Your Marks: "))
m4 = int(input("Enter Your Marks: "))
m5 = int(input("Enter Your Marks: "))
m6 = int(input("Enter Your Marks: "))
m = [m1,m2,m3,m4,m5,m6]
marks.extend(m)
marks.sort()
print(marks)


# alphabetical order
marks =[]
m1 = input("Enter Your Marks: ")
m2 = input("Enter Your Marks: ")
m3 = input("Enter Your Marks: ")
m4 = input("Enter Your Marks: ")
m5 = input("Enter Your Marks: ")
m6 = input("Enter Your Marks: ")
m = [m1,m2,m3,m4,m5,m6]
marks.extend(m)
marks.sort()
print(marks)

