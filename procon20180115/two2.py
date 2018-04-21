s = input()
t = input()

s_sorted = ''.join(sorted(s))
t_sorted = ''.join(sorted(t, reverse=True))

word_list = [s_sorted, t_sorted]
word_list.sort()

if word_list[0] == s_sorted and s_sorted != t_sorted:
    print('Yes')
else:
    print('No')
