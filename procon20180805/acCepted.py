s = input()

def check(s):
  if s[0] != 'A':
    print('WA')
    return
  
  if s[2:-1].count('C') != 1:
    print('WA')
    return
  
  s = s.strip('A')
  s = list(s)
  s.remove('C')
  s = ''.join(s)
  
  if s.islower() != True:
    print('WA')
    return
  
  print('AC')

check(s)
