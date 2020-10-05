n = int(input())
number_list = [[int(input())]]
max_length = 1
for i in range(n-1):
  temp = int(input())
  for nl in number_list:
    if nl[-1] == temp-1:
      nl.append(temp)
      length_size = len(nl)
      if length_size > max_length:
        max_length = length_size
      temp = 0
      break
  if temp != 0:
    number_list.append([temp])

print(n-max_length)

