import itertools

n, m = map(int, input().split())
p = [int(i) for i in input().split()]
evaluate = 0

numbers = []
for i in range(m):
  x, y = map(int, input().split())
  if numbers != []:
    flg = True
    for number in numbers:
      if x in number and y not in number:
        number.append(y)
        flg = False
        break
      elif x not in number and y in number:
        number.append(x)
        flg = False
        break
    if flg:
      numbers.append([x, y])
  else:
    numbers.append([x, y])

print(set(numbers))

while(len(numbers) > 1):
  numbers_length = len(numbers)
  for pair in itertools.combinations(range(len(numbers)),2):
    if set(numbers[pair[0]]) & set(numbers[pair[1]]) != set():
      numbers.append(list(set(numbers[pair[0]]) | set(numbers[pair[1]])))
      numbers[pair[0]] = []
      numbers[pair[1]] = []
      numbers = [i for i in numbers if i != []]
      break
  if numbers_length == len(numbers):
    break

for number in numbers:
  number_list = []
  for i in number:
    number_list.append(p[i-1])
  evaluate += len(set(number) & set(number_list))

print(numbers)

print(evaluate)
