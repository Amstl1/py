touple = ("1", "hello")
List = [1]
Dict = {"name": "HB", "sex": "male", touple: "per"}
Dict2 = {"ww": "123456", "name": "WYJ"}
print(Dict.values())
print(Dict.keys())
print(Dict.get(touple))
print(Dict)
print(Dict["name"])
Dict.update(Dict2)
print(Dict)
