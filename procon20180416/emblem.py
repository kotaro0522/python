import numpy

n, m = map(int, input().split())

fixed_circle = []
free_circle = []

r = []

for i in range(n):
  x, y, _r = map(int, input().split())
  r.append(_r)
  fixed_circle.append([x, y])

for i in range(m):
  x, y = map(int, input().split())
  free_circle.append([x, y])

if n == 0:
  if m == 2:
    print(numpy.linalg.norm(numpy.array(free_circle[0])-numpy.array(free_circle[1]))/2)
  else:
    minimum = 500
    for i in free_circle:
      for j in free_circle:
        length = numpy.linalg.norm(numpy.array(i)-numpy.array(j))
        if length == 0:
          continue
        elif minimum > length:
          minimum = length
        
    print(minimum/2)
elif m == 0:
  print(min(r))
else:
  for i in free_circle:
    for j in free_circle:
      length = numpy.linalg.norm(numpy.array(i)-numpy.array(j))
      if length == 0:
        continue
      elif minimum > length:
        minimum = length

  for i in range(n):
    for j in free_circle:
      length = numpy.linalg.norm(numpy.array(fixed_circle[i])-numpy.array(j)) - r[i]


  print(minimum/2)


