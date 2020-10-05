a = int(input())
b = int(input())
c = int(input())
x = int(input())

pattern = 0

for i in range(a+1):
  if 500 * i > x:
    break
  for j in range(b+1):
    if 500 * i + 100 * j > x:
      break
    for k in range(c+1):
      if 500 * i + 100 * j + 50 * k == x:
        pattern += 1
      elif 500 * i + 100 * j + 50 * k > x:
        break

print(pattern)
