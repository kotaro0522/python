import statistics
import math

n = int(input())
a = [int(i) - (index+1) for index, i in enumerate(input().split())]

abs_total = 0
for i in a:
  abs_total += abs(i)

median = statistics.median(a) 


if n % 2 == 0 and median.is_integer() is False:
  median_high = statistics.median_high(a)
  median_low = statistics.median_low(a)

  abs_high = 0
  abs_low = 0
  for i in a:
    abs_high += abs(i-median_high)
    abs_low += abs(i-median_low)

  if abs_high < abs_low:
    print(int(abs_high))
  else:
    print(int(abs_low))
else:
  abs_total = 0
  for i in a:
    abs_total += abs(i-median)
  print(int(abs_total))

