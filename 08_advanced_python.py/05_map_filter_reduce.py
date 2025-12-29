# Map Example

l = [1, 2, 3, 4, 5]

squrare = lambda x: x * x
print(list(map(squrare, l)))  # [1, 4, 9, 16, 25]
# The map function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).

print(list(map(lambda x: x * x, l)))  # [1, 4, 9, 16, 25]



# Filter Example

l = [1, 2, 3, 4, 5]

def even(n):
    if (n % 2) == 0:
        return True
    return False

onyeven = filter(even, l)
print(list(onyeven))  # [2, 4]
# The filter function constructs an iterator from elements of an iterable for which a function returns true.


# Reduce Example

l = [1, 2, 3, 4, 5]

from functools import reduce

add = lambda x, y: x + y

print(reduce(add, l))

# The reduce function applies a rolling computation to sequential pairs of values in a list. It is not a built-in function in Python 3, so you need to import it from the functools module.

# output:
1+2+3+4+5 = 15

