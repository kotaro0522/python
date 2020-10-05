a, b, n = map(int, input().split())
x = input()

for i in range(n):
  if x[i] == 'S' and a > 0:
    a -= 1
  elif x[i] == 'C' and b > 0:
    b -= 1
  elif x[i] == 'E':
    if b > a and b > 0:
      b -= 1
    elif a > 0:
      a -= 1

print(a)
print(b)
