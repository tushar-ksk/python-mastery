print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# Same task can be done like this:

for i in range(1,11):  # this means range of i is {1,2,3........(11-1)}
    print(i)           # print all the possible values of i is a single 



# for i in range(start,stop,step_size): # start is included, stop is not included.
    
        # print(i)
    
'''
output:

start
start+step_size
start+2*step_size
start+3*step_size
.
.
.
.
.
.
.
.
.
so on.

'''
# example

for x in range(0,100,10):
    print(x)

'''
output:
0
10
20
30
40
50
60
70
80
90
'''

# note: it will not print 100.