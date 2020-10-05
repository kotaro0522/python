import collections
import re

n, m = map(int, input().split())
cakes = []
x = []
y = []
z = []
for i in range(n):
  _x, _y, _z = map(int, input().split())
  if _x == 0 and _y == 0:
    cakes.append('0')
  elif _x >= 0 and _y >= 0:
    cakes.append('1')
  elif _x <= 0 and _y >= 0:
    cakes.append('2')
  elif _x <= 0 and _y <= 0:
    cakes.append('3')
  elif _x >= 0 and _y <= 0:
    cakes.append('4')
  
  if _y == 0 and _z == 0:
    cakes[-1] += '0'
  elif _y >= 0 and _z >= 0:
    cakes[-1] += '1'
  elif _y <= 0 and _z >= 0:
    cakes[-1] += '2'
  elif _y <= 0 and _z <= 0:
    cakes[-1] += '3'
  elif _y >= 0 and _z <= 0:
    cakes[-1] += '4'

  if _z == 0 and _x == 0:
    cakes[-1] += '0'
  elif _z >= 0 and _x >= 0:
    cakes[-1] += '1'
  elif _z >= 0 and _x <= 0:
    cakes[-1] += '2'
  elif _z <= 0 and _x <= 0:
    cakes[-1] += '3'
  elif _z <= 0 and _x >= 0:
    cakes[-1] += '4'
    
  x.append(_x)
  y.append(_y)
  z.append(_z)
  
print(x,y,z)
print(cakes)
count_result = collections.Counter(cakes)
print(count_result)
result_keys = [i[0] for i in count_result.most_common()]
first = result_keys[0][0]
second = result_keys[0][1]
third = result_keys[0][2]
selected_keys = []
for i in result_keys:
  if re.match(r"{0}..|.{1}.|..{2}".format(first,second,third),i):
    selected_keys.append(i)

for i, cake in enumerate(cakes):
  if cake in selected_keys:
    print(i+1,cake)

