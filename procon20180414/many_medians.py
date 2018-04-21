import copy

n = int(input())
x = [int(i) for i in input().split()]

x_original_order = copy.deepcopy(x)

x.sort()
large = x[int(n/2)]
small = x[int(n/2)-1]

for i in x_original_order:
  if i <= small:
    print(large)
  else:
    print(small)
