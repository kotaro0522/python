n = int(input())
red = []
blue = []

for i in range(n):
  a, b = map(int, input().split())
  red.append([a, b])

for i in range(n):
  c, d = map(int, input().split())
  blue.append([c, d])

print(red)
print(blue)
red.sort()
blue.sort()
print(red)
print(blue)
