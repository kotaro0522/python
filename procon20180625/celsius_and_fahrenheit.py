n = int(input())

ans = (9.0/5*n)+32

if str(ans)[-1] == '0': 
  print(int(ans))
else:
  print(ans)
