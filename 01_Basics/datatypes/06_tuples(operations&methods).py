a = (1,2,5,6,"Tushar","Rohan")
print(type(a))

b = (1)
print(type(b))

c = (1,)
print(type(c))

d = (1,4,8,3,"tushar",8,"rohan")
print(type(d))


# methods of tuple
occurance= d.count(8)
print(occurance)

index = d.index(8)
print(index)                    #report index of first occurance


# operation on tuple

# concatenation
tuple1 = (1,2,3,5,6)
tuple2 = (4,8,9,0,3,4)
r = tuple1+tuple2

# repetition
print(r)
print(tuple1*3)

# possession or membership
tup=(1,"Tushar",3,4,2,"Sharma", False, 9)
print(2 in tup)                 #boolean datatype which will report whether 2 is present in tuple or not
print(False in tup)

# length of tuple
tup=(2,3,5,1,6,7,4,2)
print(len(tup))

# min and max concept
tup=(2,3,5,6,7,4,2)
print(min(tup))
print(max(tup))                 # but when tuple contain integer data type along with string data type then < or > or = operators can't be used.

#SLICING
g = (1,2,8,4,4,5,6,6,6)
sliced= g[2:6]
print(sliced)