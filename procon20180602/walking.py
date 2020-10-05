n, d = map(int, input().split())
x = [int(i) for i in input().split()]
walk = []
answer = 0

i = 0
counter = 0
first = -1
#while counter < (n - 1):
while True:
  if x[i+1] - x[counter] <= d:
    if first >= 0:
      for j in range(len(walk)):
        if walk[j][1] == (counter+1) and x[i+1] - x[walk[j][0]-1] > d:
          answer += 1
    walk.append([counter+1, i+2])
    i += 1
  else:
    first = counter
    counter += 1
    i -= 1

  if i == (n-1):
    if counter < n - 2:
      counter += 1
      i = counter
    else:
      break

print(answer)
