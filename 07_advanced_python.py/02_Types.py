n : int = 5

name : str = "Tushar"

def sum(a: int, b: int) -> int:   # when we write sum(x,y) it will show types of x , y and overall sum that will be returned
    return a+b

print(sum(3,2))

from typing import List, Tuple, Dict

numbers: List[int] = [1,2,3,4]
print(numbers)

tup : Tuple[str,int] = ("Tushar", 1)
print(tup)