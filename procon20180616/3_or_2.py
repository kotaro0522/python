n = int(input())
ans = 0
for i in input().split():
  num = int(i)
  while num % 2 == 0:
    num /= 2
    ans += 1

print(ans)
