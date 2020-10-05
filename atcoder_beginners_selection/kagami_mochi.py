n = int(input())
d = []

for i in range(n):
  d.append(int(input()))
d.sort

level = 0

while(True):
  if len(d) == 0:
    break
  d = [i for i in d if i != d[0]]
  level += 1

print(level)  
