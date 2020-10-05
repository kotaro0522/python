import math

n = int(input())
a = [int(i) for i in input().split()]
zero = 0
for i in range(n):
  total = 0
  for j in a[i:]:
    total += j
    if total == 0:
      zero += 1

print(zero)
