n = int(input())
a = [int(i) for i in input().split()]

alice = 0
bob = 0

while(True):
  if len(a) == 0:
    break
  maximum = max(a)
  alice += maximum
  a.remove(maximum)
  if len(a) == 0:
    break
  maximum = max(a)
  bob += maximum
  a.remove(maximum)

print(alice-bob)
