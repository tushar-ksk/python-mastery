
with open("this.txt") as f:
    content1 =  f.read()

with open("copy.txt") as g:
    content2 = g.read()


if content1 == content2 :
    print("YES, these files are identical.")

else:
    print("NO, these files are identical.")
