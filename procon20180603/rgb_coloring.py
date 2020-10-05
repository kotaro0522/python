n, a, b, k = map(int, input().split())

if k == 0:
  print(1)
else:
  ans = 0
  pattern_number = pow(4,n)
  for i in range(pattern_number+1):
    pass
    score = 0
    while i > 0:
      x = str(i%4)
      if x == '1':
        score += a
      elif x == '2':
        score += (a+b)
      elif x == '3':
        score += b
      i = int(i/4)
    if score == k:
      ans += 1

  print(ans%998244353)


