n = input()
sn = 0
for i in n:
  sn += int(i)

if int(n) % sn == 0:
  print('Yes')
else:
  print('No')

