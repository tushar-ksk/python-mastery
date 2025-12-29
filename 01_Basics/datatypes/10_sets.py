# set is a well defined collection of item without repetition.

s = {1,2,4,5,5,5,3,9,9,9,9,9}
print(type(s))
print(s) # it prints {1, 2, 3, 4, 5, 9} but if s would a lists = [1,2,4,5,5,5,3,9,9,9,9,9] then if will print [1,2,4,5,5,5,3,9,9,9,9,9] 
print(len(s))




# difference between empty dict and empty set
e = {} # empty dict
print(e,type(e))

f = set() # empty set
print(f,type(f))

f.add("tushar")
print(f)

print(s.difference({9}))


# PROPERTIES OF SETS

#sets do not contain duplicate value
#sets are unordered.
#sets are unindexed, we canot access item by index.
# we can't change prexisting item in sets
# but we can add or remove items from sets