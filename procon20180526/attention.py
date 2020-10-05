# brute-force search is slow...

n = int(input())
s = input()
min_people = n - 1

def we_counter(pos):
  front = s[:pos]
  back = s[pos+1:]
  people = front.count('W') + back.count('E')
  return people


for i in range(n):
  people = we_counter(i)

  if people < min_people:
    min_people = people

print(min_people)
