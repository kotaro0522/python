n = int(input())
total = 0
for i in range(n):
    seats = [int(j) for j in input().split()]
    total = total + seats[1] - seats[0] + 1
print(total)
