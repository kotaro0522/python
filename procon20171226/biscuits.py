import itertools

N, P = [int(i) for i in input().split()]
biscuits = [int(i) for i in input().split()]
even = 0
odd = 0
buffer_count = 1
even_c = 1

for i in biscuits:
    if i % 2 == 0:
        even += 1
    elif i % 2 == 1:
        odd += 1

if P == 0:
    # even
    odd_c = 1
elif P == 1:
    # odd
    odd_c = 0

if even > odd:
    for i in range(1, even+1):
        even_c += 2 ** (i-1)
        if i == odd:
            buffer_count = even_c
elif odd >= even:
    for i in range(1, odd+1):
        buffer_count += 2 ** (i-1)
        if i == even:
            even_c = buffer_count

if P == 0:
    # even
    if buffer_count > 2:
        odd_c = (buffer_count / 2)
elif P == 1:
    # odd
    if buffer_count > 1:
        odd_c = (buffer_count / 2)

print(int(even_c * odd_c))
