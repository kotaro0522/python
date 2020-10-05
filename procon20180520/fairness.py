a, b, c, k = map(int, input().split())

if abs(a - b) <= pow(10,18):
  if k % 2 == 0:
    print(a-b)
  else:
    print(b-a)
else:
  print('Unfair')
