import itertools

n, k = map(int, input().split())

number = list(range(1,n+1))

num_list = list(itertools.product(number, repeat=3))

count = 0

for num_comb in num_list:
  #print(num_comb)
  if (num_comb[0] + num_comb[1]) % k == 0 and (num_comb[1] + num_comb[2]) % k == 0 and (num_comb[2] + num_comb[0]) % k == 0:
    count += 1

#print(num_list)
print(count)
