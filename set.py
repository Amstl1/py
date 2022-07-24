import sys

LIST = [1, 3, 2, 2, 2, 2, 2]
DICT = {"A": "a", "B": "b"}
Set = set(("hello",))
print(Set)
Set.update({"hello", "world"})
print(Set)
Set.update("helloworld")
print(Set)
it = iter(LIST)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
