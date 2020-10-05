x = int(input())
maximum = 1
for i in range(2,32):
  if i*i <= x and i*i > maximum:
    maximum = i*i

for i in range(2, 11):
  if pow(i,3) <= x and pow(i,3) > maximum:
    maximum = pow(i,3)

for i in range(2, 6):
  if pow(i,4) <= x and pow(i,4) > maximum:
    maximum = pow(i,4)

for i in range(2, 4):
  if pow(i,5) <= x and pow(i,5) > maximum:
    maximum = pow(i,5)

for i in range(2, 4):
  if pow(i,6) <= x and pow(i,6) > maximum:
    maximum = pow(i,6)

for i in range(7,10):
  if pow(2,i) <= x and pow(2,i) > maximum:
    maximum = pow(2,i)

print(maximum)
