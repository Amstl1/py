###### StringIO ########
import json
import os
import pickle
from io import StringIO

f = StringIO()
f.write('hello')
f.write("    ")
f.write('WORLD')
print(f.getvalue())

####### BytesIO #######
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('GBK'))
print(f.getvalue())

##### OS ###########
print(os.path.abspath('./'))

###### pickle.dump #########
d = dict(name='jj', sex='male', age='11')
print(type(d))
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

##### pickle.load #########
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

##### json.dumps########
d = dict(name='jj', sex='male', age='11')
print(type(json.dumps(d)))

##### json.load #########
d = dict(name='jj', sex='male', age='11')
print(type(d))
z = str(d)
print(z)

#print(type(json.loads(z)))


