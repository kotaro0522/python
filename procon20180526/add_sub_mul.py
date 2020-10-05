a, b = map(int, input().split())

ans1 = a + b
ans2 = a - b
ans3 = a * b

if ans1 > ans2:
  if ans1 > ans3:
    print(ans1)
  else:
    print(ans3)
else:
  if ans2 > ans3:
    print(ans2)
  else:
    print(ans3)
