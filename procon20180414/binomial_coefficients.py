n = int(input())
a = [int(i) for i in input().split()]

a.sort()

if n == 2:
  print(str(a[1])+" "+str(a[0]))
else:
  maximum = a[-1]
  a.pop()
  half = maximum/2
  a.append(half)
  a.sort()

  position = a.index(half)

  if position+1 >= len(a):
    print(str(maximum)+" "+str(int(a[position-1])))
    exit()
  else:
    large = int(a[position+1])
  if position-1 <= 0:
    print(str(maximum)+" "+str(int(a[position+1])))
    exit()
  else:
    small = int(a[position-1])

  if large - (half) < (half) - small:
    print(str(maximum)+" "+str(large))
  else:
    print(str(maximum)+" "+str(small))
