numbers = [int(i) for i in input().split()]
a = []
for i in numbers:
    cnt=0
    for j in numbers:
        if i == j:
            continue
        if i > j:
            cnt+=1
    a.append(cnt)
print(a)