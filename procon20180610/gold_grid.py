n, color = map(int, input().split())
d = []
c = []
for i in range(color):
  d.append([int(i) for i in input().split()])

for i in range(n):
  c.append([int(i) for i in input().split()])

print(d)
print(c)
