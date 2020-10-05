n = int(input())
a = [int(i) for i in input().split()]

def shift(a):
  count = 0
  while(True):
    for i in a:
      if i % 2 != 0:
        return count
    count += 1
    a = [int(i/2) for i in a]

print(shift(a))
