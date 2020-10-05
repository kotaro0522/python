number_map = [int(i) for i in input().split()]
n = int(input())
number_list = [int(input())]

for loop_num in range(n-1):
  flg = False
  str_i = input()
  i = int(str_i)
  for index, j in enumerate(number_list):
    str_j = str(j)
    if len(str_i) > len(str_j):
      continue
    elif len(str_i) < len(str_j) or i == j:
      number_list.insert(index, i)
      break
    else:
      for index_k, k in enumerate(str_i):
        l = str_j[index_k]
        if k == l:
          continue
        if number_map.index(int(k)) < number_map.index(int(l)):
          flg = True
          number_list.insert(index, i)
          break
        else:
          break
    if flg:
      break
  else:
    number_list.append(i)

for i in number_list:
  print(i)

