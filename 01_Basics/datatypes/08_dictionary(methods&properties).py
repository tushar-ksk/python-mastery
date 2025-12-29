# # Dictionary

marks = {
    "Tushar": 78,
    "Soham" : 98,
    "ramfal": 67
}

print(marks, type(marks))
print(len(marks))


# in strings, list, tuple we use 'index number' to refer a 'value'.
# print(marks[0]) tihs will give error when marks is dictionary datatype.


# whereas in dictionary we use 'key' to refer 'value'.
print(marks["Soham"])

# dictionaries are mutable, unordered, indexed.
# dictionaries cannot contain duplicate keys

d = {} # empty dict

# methods of dictionary

stud={
    "Name": "Ramfal",
    "class": "12th",
    "Rollno.": 23,
    "marks": 78
}

print(stud.items())                 # this reports list of key value order pair of dict.
print(stud.keys())
print(stud.values())


stud.update({"class": "11th", "address": "haryana" })
print(stud)


print(stud.get("Name")) 
print(stud["Name"])

# difference between get method and print(stud["Name"]) is :
# get method prints None when key in not present in dict
# print(stud["key"]) gives an error


stud.pop("Rollno.")                 # termimnate Rollno. key from dict
print(stud)


stud.popitem()                      # remove last item first in last out method
print(stud)

stud.popitem()
print(stud)



