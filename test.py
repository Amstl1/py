# -*- coding: UTF-8 -*-

"""
def Count():
    str1 = input("please input:\n")
    str2 = input("please input subst:\n")
    mcount = 0
    mcount = str1.count(str2)
    print(mcount)

Count()


# 2-------------------------


def Time():
    import time
    st = time.perf_counter()
    print(st)
    for i in range(5):
        print(i)


Time()


ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ma[-1])
col1 = [row[1] for row in ma]
print(col1)
col2 = [row[1] for row in ma if row[1] % 2 == 0]
print(col2)


import random

for i in range(3, -1, -1):
    print(i)




class xxxxx:
    x = 0
    y = 2


def ff(self):
    self.x = 20
    self.y = 200


a = xxxxx()
a.x = 3
a.y = 'z'
print(type(a.y))
ff(a)
print(type(a.y))
print("a.x = %d,a.y=%s" % (a.x, a.y))

str1 = 'q21313'
str2 = '23123'
str3 = 'adad'
str4 = ''
#str4 = str1 + str2 + str3
print(str4)

str4 = str4.join(str1)


OCT = input("oct number is :")
print(len(OCT))
n = 0
sum = len(OCT)
for i in range(len(OCT)):
    print(int(OCT[i]))
    n += int(OCT[i]) * (8 ** (sum-1))
    sum = sum - 1
print(n)



person = {"ww": 10, "hh": 13, "zz": 20}
kk = 'ww'
for key in person.keys():
    if person[key] > person[kk]:
        kk = key

print("name = %s,age = %s" % (kk, person[kk]))




s = [12, 2, 2, 2, 2, 2, 2, 2, 2]
for i in len(s):
    print(s[i])

"""

import openpyxl
import json
import ITER
import zipfile
import requests

def Prs_json():
    json.dump()
