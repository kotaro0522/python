import math

n = int(input())
zero = 0
total_dictionary = {0: 1}
total = 0

for i in input().split():
  total += int(i)
  zero += total_dictionary.get(total,0)
  if total in total_dictionary:
    total_dictionary[total] += 1
  else:
    total_dictionary[total] = 1

print(zero)
