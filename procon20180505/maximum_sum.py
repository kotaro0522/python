number = [ int(i) for i in input().split()]
k = int(input())

max_num = max(number)
number.remove(max_num)

max_num = max_num * (2 ** k)

print(sum(number)+max_num)
