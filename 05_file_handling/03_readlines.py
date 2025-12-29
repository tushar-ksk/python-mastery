str = '''Hello MY friends.
My name is Tushar Sharma.
Today I am learing Python.
Just for fun.'''

f = open("file_2.txt","w")
f.write(str)
f.close()

f = open("file_2.txt","r")
lines = f.readlines()
print(lines,type(lines))
f.close