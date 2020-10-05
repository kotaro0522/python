a, b = map(int, input().split())

diff = b - a
ans = 0
for i in range(diff):
  ans += i
ans -= a
print(ans)
