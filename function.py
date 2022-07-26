from collections.abc import Iterable


####### map ###############
def ff(x):
    return x * x


z = map(ff, [1, 2, 3, 4, 5])
print(isinstance(z, Iterable))
# print(list(z))
for i in z:
    print(i)

###### reduce ############
from functools import reduce


def add(x, y):
    return x + y


z = reduce(add, [1, 2, 3, 4])
print(isinstance(z, Iterable))
print(z)


###### filter ############
def is_odd(n):
    return n % 2 == 1


b = list(filter(is_odd, [1, 2, 3, 4, 5]))

print(b)

