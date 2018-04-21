n, x = map(int, input().split())
m = []
for i in range(n):
  m.append(int(input()))
  x -= m[i]

if x > 0:
  n += int(x / min(m))

print(n)
