dict1 = {"a" : 3, "b" : 4}    # "b" : 4 of dict1 is ignored because key "b" is also present in dict2
dict2 = {"b" : 5, "c" : 6}
c = dict1|dict2
print(c)