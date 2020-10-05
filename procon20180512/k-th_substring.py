s = input()
k = int(input())
number = len(s)
word_list = []
for i in range(number):
  for j in range(1,6):
    if i+j > number:
      break
    word_list.append(s[i:i+j])

unique_list = list(set(word_list))

print(sorted(unique_list)[k-1])
