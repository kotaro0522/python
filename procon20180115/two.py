s = input()
t = input()

s_sorted = sorted(s)
t_sorted = sorted(t)

try:
    for i in s_sorted:
        for j in t_sorted:
            if i < j:
                print('Yes')
                raise Exception
            elif i == j:
                t_sorted.remove(i)
                break
        else:
            print('No')
            raise Exception
    if t_sorted != []:
        print('Yes')
    else:
        print('No')
except Exception:
    pass
