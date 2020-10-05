n = int(input())

a = [int(i) for i in input().split()]

# n が 2なら 大きい方を出力して終わり

#def euclid(m, n):
#  if n == 0:
#    return m
#  new_m = n
#  new_n = m % n
#  return euclid(new_m, new_n)
#
#def array_euclid(numbers):
#  n = len(numbers)
#  v = numbers[n-1] % numbers[n-2]
#  if v == 0:
#    if n == 2:
#      return numbers[0]
#    
#    numbers.pop()
#    return array_euclid(numbers)
#
#  numbers[n-1] = numbers[n-2]
#  numbers[n-2] = v
#  return array_euclid(numbers)

#print(array_euclid(a))

#if n == 2:
#  print(euclid(a[0], a[1]))
#if n > 2:
#  max_list = []
#  max_list.append(array_euclid(a[:]))
#  for i in range(n):
#    a2 = a[:]
#    a2.pop(i)
#    max_list.append(array_euclid(a2))
#  print(max(max_list))
#


# n が3になるまでやって、大きい方が答え？

#for i in range(n-1):


#print(euclid(a[0],a[1]))


# 最大公約数を求めるには math.gcd を使う

from fractions import gcd
from functools import reduce

def gcd_list(numbers):
  if len(numbers) == 0: return 0
  return reduce(gcd, numbers)

#print(gcd_list([0, 100]))

max_list = []
max_list.append(gcd_list(a))
#gcd_max = gcd_list(a)
for i in range(n):
  a2 = [gcd_list(a[0:i]), gcd_list(a[i+1:])]
  #a2.pop(i)
  max_list.append(gcd(gcd_list(a[0:i]), gcd_list(a[i+1:])))
print(max(max_list))

