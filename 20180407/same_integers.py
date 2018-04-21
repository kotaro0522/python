import math

number_list = [int(i) for i in input().split()]

even_counter = 0

for i in number_list:
  if i % 2 == 0:
    even_counter = even_counter + 1

def even_checker(n_list):
  for i in n_list:
    if i % 2 == 0:
      return i

def odd_checker(n_list):
  for i in n_list:
    if i % 2 == 1:
      return i

if even_counter == 3 or even_counter == 0:
  goal = max(number_list)
  number_list.remove(goal)
  bigger = max(number_list)
  smaller = min(number_list)
  first_count = 0
else:
  if even_counter == 2:
    alone = odd_checker(number_list)
  elif even_counter == 1:
    alone = even_checker(number_list)
  number_list.remove(alone)
  bigger = max(number_list)
  smaller = min(number_list)
  if bigger > alone:
    first_count = math.ceil((bigger - alone)/2)
    goal = alone + first_count * 2
  else:
    first_count = 0
    goal = alone

second_count = goal - bigger
third_count = int((goal - (smaller + second_count))/2)

print(first_count+second_count+third_count)

#print(first_count)
#print(second_count)
#print(third_count)

#print(alone)

#print(even_counter)

#print(number_list)
