n = int(input())
money_list = (59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1)
ans = 0
for i in money_list:
  while n >= i:
    if (46656*2) <= n:
      n -= 46656
      ans += 1
    elif (6561*2) <= n < (7776+6561) or (6561*3) <= n <= (6561*3+1296):
      n -= 6561
      ans += 1
    elif (729*2) <= n < (1296+729) or (729*3) <= n < (1259+729+216):
      n -= 729
      ans += 1
    elif (81*3) <= n <= (81*3+2) or (81*3+6) <= n < (216+36): #249: #(245):
      n -= 81
      ans += 1
    elif 12 <= n < 15:
      n -= 6
      ans += 1
    else:
      n -= i
      ans += 1

print(ans)
