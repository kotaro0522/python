n, y = map(int, input().split())

def otoshidama(n, y):
  def total(x, y, z):
    return 10000*x + 5000*y + 1000*z

  for i in range(int((n+1)/3+1)):
    for j in range(int((n+1)/2+1)):
      if i + j > n:
        break
      k = n - i - j
      if total(i, j, k) == y:
        print("{} {} {}".format(i, j, k))
        return
      elif total(k, j, i) == y:
        print("{} {} {}".format(k, j, i))
        return
      elif total(j, k, i) == y:
        print("{} {} {}".format(j, k, i))
        return
      elif total(i, k, j) == y:
        print("{} {} {}".format(i, k, j))
        return
      elif total(k, i, j) == y:
        print("{} {} {}".format(k, i, j))
        return
      elif total(j, i, k) == y:
        print("{} {} {}".format(j, i, k))
        return
  
  print("-1 -1 -1")

otoshidama(n, y)
