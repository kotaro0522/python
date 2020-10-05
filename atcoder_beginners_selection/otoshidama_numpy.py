import numpy as np

n, y = map(int, input().split())
y = int(y / 1000)
def otoshidama(n, y):
  bill = np.array([10, 5, 1])

  for i in range(int((n+1)/3+1)):
    for j in range(int((n+1)/2+1)):
      if i + j > n:
        break
      k = n - i - j
      number = np.array([[i, k, j, i, k, j], [j, j, k, k, i, i], [k, i, i, j, j, k]])
      result = np.dot(bill, number)
      if result[0] == y:
        print("{} {} {}".format(i, j, k))
        return
      elif result[1] == y:
        print("{} {} {}".format(k, j, i))
        return
      elif result[2] == y:
        print("{} {} {}".format(j, k, i))
        return
      elif result[3] == y:
        print("{} {} {}".format(i, k, j))
        return
      elif result[4] == y:
        print("{} {} {}".format(k, i, j))
        return
      elif result[5] == y:
        print("{} {} {}".format(j, i, k))
        return
  
  print("-1 -1 -1")

otoshidama(n, y)
