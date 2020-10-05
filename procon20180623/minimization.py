n, k = map(int, input().split())
input()
n -= k
ans = 1
while n > 0:
  n -= (k - 1)
  ans += 1

print(ans)
