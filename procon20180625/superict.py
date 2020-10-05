import re

s = input()

if re.search(r'.*[Ii].*[Cc].*[Tt]', s) is not None:
  print('YES')
else:
  print('NO')

