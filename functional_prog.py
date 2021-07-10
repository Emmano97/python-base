"""
letters = ["a", 'b', 'c', 'd']

second_letters = ["a", 'b', 'c', 'd']


it = iter(letters)

zipped = zip(letters, second_letters)

print(zipped is iter(zipped))

while True:
    try:
        print(next(zipped))
    except StopIteration:
        break

"""
"""
import itertools

for x in itertools.chain((1, 2, 3), [1, 4, 6], {'id':4, 'name':"emmano"}):
    print(x)

"""

"""
square = lambda x: x**2

print(square(4))

def image(func):
    for x in range(2, 20):
        print(f"f(x): {func(x, x-1):0.2f}\n")

mapped = map(square, range(20))

filtered = filter(lambda x: x%2==0, range(20))

#image(lambda x, y: x**y - 1)

print(mapped)
"""

from functools import reduce
from operator import mul, itemgetter, 


def factorial(n):
    return reduce(mul, range(1, n+1), 1)

#print(factorial(5))

cords = [(43, 7),  (46, -7), (46, 0), (47, 5)]


cords.sort(key=itemgetter(1))

print(cords)

tuple([1, 2, 3])