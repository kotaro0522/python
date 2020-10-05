test_dic = {0: 1}

print(test_dic[0])
total=2
test_dic[0] += 1

print(test_dic[0])
total += test_dic.get(total,0)
if 1 in test_dic:
  test_dic[1] += 1
else:
  test_dic[1] = 1
print(test_dic[1])
