# cumulative sum algorithm is faster than brute-force search!

n = int(input())
s = input()
point = [0]

def we_counter(pos):
  front = s[:pos]
  back = s[pos+1:]
  people = front.count('W') + back.count('E')
  return people


for i in range(n):
  if s[i] == 'W':
    point.append(point[i]-1)
  else:
    point.append(point[i]+1)

# pos = 7, 3 + 3
max_point = max(point)
pos = point.index(max_point)
front_num = int(pos/2) + max_point
print(front


print(we_counter(pos))
