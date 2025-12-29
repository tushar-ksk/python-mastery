list1 = [5, 10, 15, 26, 34, 45, 56, 67, 35, 100, 123,42,43,53,49,8,237,4,72,98,42,2,9,85,]
def greatest(a,b):
    if a>b:
        return a
    return b
from functools import reduce

print(reduce(greatest,list1))