a, b = map(int, input().split())

a_mod = a % 12
b_mod = b % 12

price = (int(a/12)+int(b/12))*7200

if a_mod in range(2,6):
  if b_mod in range(2,6) and a_mod>b_mod or b_mod in range(8,11) and a_mod>(b_mod-6):
    first = b_mod
    second = a_mod
    order = b,a
  else:
    first = a_mod
    second = b_mod
    order = a,b
elif a_mod in range(8,11):
  if b_mod in range(2,6) and (a_mod-6)>b_mod or b_mod in range(8,11) and (a_mod-6)>(b_mod-6):
    first = b_mod
    second = a_mod
    order = b,a
  else:
    first = a_mod
    second = b_mod
    order = a,b
elif b_mod in range(2,6) or b_mod in range(8,11):
  first = b_mod
  second = a_mod
  order = b,a
else:
  first = a_mod
  second = b_mod
  order = a,b

first_order = []
second_order = []

if order[0] == 0:
  first_order.append(0)
elif first == 1:
  price += 880
  first_order.append(1)
elif first in range(2,6):
  price += (first-1) * 880
  first_order += [1] * first
elif first == 6:
  price += 4080
  first_order.append(6)
elif first == 7:
  price += 4960
  first_order = [1, 6]
elif first in range(8,11):
  price += 4080+(first-7)*880
  first_order += [1] * (first-6)
  first_order.append(6)
else:
  price += 7200
  first_order.append(12)

if order[0] > 0:
  first_order += [12] * int(order[0]/12)

if order[1] == 0:
  second_order.append(0)
elif second in range(1,5):
  price += second * 880
  second_order += [1] * second
elif second in range(5,7):
  price += 4080
  second_order.append(6)
elif second in range(7,10):
  price += 4080+(second-6)*880
  second_order += [1] * (second-6)
  second_order.append(6)
elif second in range(10,13):
  price += 7200
  second_order.append(12)

if order[1] > 0:
  second_order += [12] * int(order[1]/12)

print(price)
print(' '.join(map(str, first_order)))
print(' '.join(map(str, second_order)))
