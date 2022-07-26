g = [x * x for x in range(10)]
z = (x * x for x in range(10))
print(z)

from collections.abc import Iterable

from collections.abc import Iterator
from functools import reduce
print(isinstance(iter("[]"), Iterable))


def ff(x):
    return x * x

print(isinstance(ff, Iterator))
r = map(ff, [1, 2, 3, 4, 5])
print(list(r))

print(reduce(sum, [1, 2, 3, 4]))