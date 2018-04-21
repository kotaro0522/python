num = int(input())
list = []
for i in range(num):
    word = input()
    if word in list:
        list.remove(word)
    list.insert(0, word)
for answer in list:
    print(answer)
