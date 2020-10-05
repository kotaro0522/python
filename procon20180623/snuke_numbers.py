k = int(input())

for i in range(1,k+1):
  top_number = i % 9
  if top_number == 0:
    top_number = ''
  number_of_nine = int(i/9)
  number = str(top_number)+'9'*number_of_nine
  if i >= 136:
    break
  else:
    print(number)

