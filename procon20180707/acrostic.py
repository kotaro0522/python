import math

s = input()
w = int(input())

times = math.ceil(len(s)/w)
ans = ''
for i in range(times):
  ans += s[i*w]

print(ans)

