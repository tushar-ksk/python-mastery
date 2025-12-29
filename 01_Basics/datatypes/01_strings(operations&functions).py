# String length

a= "tushar sharma"
print(len(a))


#String Slicing

fullname= "tushar sharma"
lastname = fullname[7:13]           # from 7 to 13-1=12
print(lastname)


# negative slicing
firstname = fullname[0:-7]          #start from index 0 to all the way till 7 from last,,, counting starts from -1 if starts from last and from 0 if starts from begining.

# blank index
print(fullname[:])                  #this  means form 0 to len-1
print(fullname[:-9])                # from 0 to len-1-9
print(fullname[-5:])                # from len-1-5 to len-1
print(fullname[5:])                 # from 5 to len-1


# slicing with skip value
a= "skhadjsahakjdfhkshkjh"
print(a[1:14:2])                    # start from index 1 ends at index 13 skip 1 letter after every letter


# STRINGS FUNCTION
a = "tushar sharma Kaushik"
print(len(a))                       # return int data type
print(a.endswith("ar"))             # boolean data type
print(a.endswith("ma"))
print(a.startswith("tu"))
print(a.startswith("flu"))
print(a.capitalize())               # capitalize only first letter
print(a.upper())                    # convert whole string in upper case
print(a.lower())                    # convert whole string in lower case
print(a.title())                    # capitalize only first letter of every word
print(a.find("sharma"))             # print the index of s
b= "tushar is a good good boy"
print(b.replace("good","bad"))
