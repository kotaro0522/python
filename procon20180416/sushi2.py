n, t = map(int, input().split())
a = [int(i) for i in input().split()]
time = a[0]
a.pop(0)

for i in a:
  how_many = 0
  while(True):
    if i + t*how_many > time:
      time = i +t*how_many
      break
    else:
      how_many += 1

print(time)
