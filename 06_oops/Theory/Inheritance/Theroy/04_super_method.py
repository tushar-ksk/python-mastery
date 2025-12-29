class hello:
    a = 1
    def __init__(self):
        print("This is the constructor of hello")

class hey(hello):
    b = 2
    def __init__(self):
        print("This is the constructor of hey")
class bye(hey):
    c = 3
    def __init__(self):
        super().__init__()
        print("This is the constructor of bye")



p = hey()
print(p.a, p.b)
 
'''
output:
This is the constructor of hey
1 2
'''

p = bye()
print(p.a,p.b,p.c)

'''
output:
This is the constructor of hey
This is the constructor of bye
1 2 3
'''
