n = int(input())
ans = 0

for i in str(n):
  ans += int(i)

if ans == 1:
  print(10)
else:
  print(ans)
