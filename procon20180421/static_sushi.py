import copy
#import time
#import pdb;pdb.set_trace()

n, c = map(int, input().split())

x = []
v = []

for i in range(n):
  _x, _v = map(int, input().split())
  
  x.append(_x)
  v.append(_v)

#t1 = time.time()

x.insert(0, 0)
v.insert(0, 0)

reverse = [0, 0]

def find_sushi(x, v, c, pos, cal, max_cal, route):
  if len(x) == 1:
    return max_cal
  x.pop(0)
  v.pop(0)
  max_cal1 = 0
  max_cal2 = 0
  if route != 'right_left':
    if route == 'first':
      route1 = 'right'
    elif route == 'left':
      route1 = 'left_right'
    else:
      route1 = route
    x1 = copy.deepcopy(x)
    v1 = copy.deepcopy(v)
    cal1 = cal
    if x1[0] > pos:
      cal1 += v1[0] - (x1[0] - pos)
    else:
      cal1 += v1[0] - (c - pos + x1[0])
    if cal1 > max_cal:
      max_cal = cal1
    max_cal1 = find_sushi(x1, v1, c, x1[0], cal1, max_cal, route1)
  if route != 'left_right':
    if route == 'first':
      route2 = 'left'
    elif route == 'right':
      route2 = 'right_left'
    else:
      route2 = route
    x2 = copy.deepcopy(x)
    v2 = copy.deepcopy(v)
    cal2 = cal
    x2.insert(0, x2[-1])
    x2.pop()
    v2.insert(0, v2[-1])
    v2.pop()
    if x2[0] > pos:
      cal2 += v2[0] - (c + pos - x2[0])
    else:
      cal2 += v2[0] - (pos - x2[0])
    if cal2 > max_cal:
      max_cal = cal2
    max_cal2 = find_sushi(x2, v2, c, x2[0], cal2, max_cal, route2)
  
  if max_cal1 > max_cal2:
    return(max_cal1)
  else:
    return(max_cal2)

print(find_sushi(x, v, c, 0, 0, 0, 'first'))

#t2 = time.time()

#total_time = t2 - t1
#print(total_time)
