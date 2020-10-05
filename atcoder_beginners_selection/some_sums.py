n, a, b = map(int, input().split())

total_sum = 0

for i in range(1,n+1):
  number = str(i)
  total = 0
  for j in number:
    total += int(j)
  if total >= a and total <= b:
    total_sum += i

print(total_sum)
