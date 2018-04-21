list = [int(i) for i in input().split()] 

if list[1] >= list[2]:
    print("delicious")
elif list[1]+list[0] >= list[2]:
    print("safe")
else:
    print("dangerous")
