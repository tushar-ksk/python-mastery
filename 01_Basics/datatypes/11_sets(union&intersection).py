s1={2,5,8,9,4,6,}
s2={5,7,1,3.4,6,6,6}


# union print a set containing values of both sets without repeating values
s3= s1.union(s2)
# s3= s1.union(s2) = s2.union(s1)
print(s3)



#intersection prints a set containing values which are common in both sets called overlapping values.
print(s2.intersection(s1))
# print(s1.intersection(s2)) = print(s2.intersection(s1))

s3.remove(6)
print(s3)

s3.clear()
print(s3)


print(s1.issubset(s3))