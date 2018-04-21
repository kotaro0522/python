n, m, x = map(int, input().split())
a = [int(i) for i in input().split()]

a.append(x)
a.sort()
position = a.index(x)+1

if position == 0 or position == m+1:
  print(0)
else:
  if (m+1)-position <= (m+1)/2:
    print(m+1-position)
  else:
    print(position-1)

