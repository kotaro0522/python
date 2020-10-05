n = int(input())

v = [int(i) for i in input().split()]

c = [int(i) for i in input().split()]

total = 0

for i in range(n):
  if v[i] > c[i]:
    total += (v[i] - c[i])

print(total)
