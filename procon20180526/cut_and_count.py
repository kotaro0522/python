import collections

n = int(input())
s = input()
max_number = 0

for i in range(n-1):
  front = collections.Counter(s[:i+1])
  back = collections.Counter(s[i+1:])
  number = len(front.keys() & back.keys())
  if number > max_number:
    max_number = number

print(max_number)
