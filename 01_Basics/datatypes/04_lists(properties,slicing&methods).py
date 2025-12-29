friends= ["Apple","kiwi",5,8,"Tushar", True, "Notebook"]

print(friends[0])                   # this reports zeroth element of string
friends[0]= "sandwich"


# unlike strings, lists are mutable
print(friends[0])                   #this will report sandwich therefore it will report sandwich


# lists slicing
print(friends[1:4])                 #from first position to 4-1 th position



#lists methods

# 1. append

friends= ["Apple","kiwi",5,8,"Tushar", True, "Notebook"]
print(friends)

friends.append("Kaushik")           #add element at end of the list
print(friends)



# 2. sort and reverse

l1 = [5,6,48,2,246,55,2,8,8,9,58,6]
l1.sort()                           #sort list in increasing order
print(l1)
l1.reverse() #decreasing order
print(l1)



# 3. pop

l2=[5,6,48,2,24,3,37,6,55,2,8,8,9,58,6]
print(l2)
print(l2.pop(2)) #report element of 2nd index
l2.pop(2) #remove element of second index
print(l2)



# 4. remove and clear

l2.remove(8) #removes itm 8 from its first occurance.
print(l2)
print(l2.count(6)) #it reports how many times 6 came in lists

l2.clear() #removes all the items of lists
print(l2)

  


# 5. insert and pop

l3 = [5,6,4,88,9,23,3,75,51,0]
l3.insert(2, 18)  #insert 18 in list where index is 2


print(l3)
print(l3.pop(2)) #method is applied on modified list
