#import itertools

n, m, d = map(int, input().split())

#numbers = (int(i) for i in range(1,n+1))
#beauties = []
#
#for i in itertools.product(numbers, repeat=m):
#  print(i)
#  point = 0
#
#  for j in range(len(i)-1):
#    if abs(i[j] - i[j+1]) == d:
#      point += 1
#  beauties.append(point)
#
#print(sum(beauties)/len(beauties))
if d != 0:
  print((0.5 / (n / 2) ** 2) * (m - 1) * (n - d))
else:
  print((0.5 / (n / 2) ** 2) * (m - 1) * (n - d) / 2)

