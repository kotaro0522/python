d, g = map(int, input().split())

p = []
c = []
t = []

for i in range(d):
  _p, _c = map(int, input().split())
  p.append(_p)
  c.append(_c)
  t.append([(100 * (i+1) * _p + _c) / _p, _p,(100 * (i+1) * _p + _c), i+1])

x = []

for i in range(1, d+1):
  x.append([i*100, 0, t[i-1][2], i])

checked = []
total = 0
number = 0
count = 0
all_list = sorted(x+t), reverse=True)

for i in all_list:
  if i[1] != 0:
    if total + i[2] > g:
      if number == 0:
        number = count + i[1]
  else:

  

