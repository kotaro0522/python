a, b, k = map(int, input().split())

for i in range(k):
  print(a)
  a = a + 1
  if a > b:
    break
if a > (b - k + 1):
  large_start = a
else:
  large_start = b - k + 1

for i in range(k):
  if large_start > b:
    break
  print(large_start)
  large_start = large_start + 1
