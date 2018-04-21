n = int(input())
d, x = map(int, input().split())
a = []
for i in range(n):
  a.append(int(input()))

chocolate = x

for i in a:
  chocolate += 1
  days = 1
  while(True):
    days += i
    if days <= d:
      chocolate += 1
    else:
      break

print(chocolate)
